import json
from enum import Enum
from pathlib import Path

import numpy as np
import pdal
import rasterio

from lidar_qc.log import get_logger

logger = get_logger()


class DensityFilter(str, Enum):
    """
    Assigning commandline filter inputs to variables.
    """

    common = "common"
    common_no_flag = "common_no_flag"
    all = "all"
    pulse = "pulse"
    ground = "ground"
    low_veg = "low_veg"
    buildings = "buildings"
    unclassified = "unclassified"
    noise = "noise"
    point = "point"
    withheld = "withheld"
    overlap = "overlap"
    ground_no_flag = "ground_no_flag"
    low_veg_no_flag = "low_veg_no_flag"
    buildings_no_flag = "buildings_no_flag"
    unclassified_no_flag = "unclassified_no_flag"
    noise_no_flag = "noise_no_flag"
    noise_with_withheld = "noise_with_withheld"
    all_veg = "all_veg"
    medium_veg = "medium_veg"
    high_veg = "high_veg"
    intensity = "intensity"
    bridge = "bridge"
    water = "water"
    all_veg_no_flag = "all_veg_no_flag"
    medium_veg_no_flag = "medium_veg_no_flag"
    high_veg_no_flag = "high_veg_no_flag"
    bridge_no_flag = "bridge_no_flag"
    water_no_flag = "water_no_flag"
    colourised = "colourised"


# Filters that need colour in the point format (PDRF 2, 3, 5, 7, 8 or 10).
DENSITY_FILTER_COLOUR: list[DensityFilter] = [
    DensityFilter.colourised,
]
COLOUR_PDRFS = {2, 3, 5, 7, 8, 10}
NIR_PDRFS = {8, 10}


DENSITY_FILTER_COMMON: list[DensityFilter] = [
    DensityFilter.pulse,
    DensityFilter.ground,
    DensityFilter.low_veg,
    DensityFilter.buildings,
    DensityFilter.unclassified,
    DensityFilter.noise,
    DensityFilter.intensity,
]

DENSITY_FILTER_COMMON_NO_FLAG: list[DensityFilter] = [
    DensityFilter.ground_no_flag,
    DensityFilter.low_veg_no_flag,
    DensityFilter.buildings_no_flag,
    DensityFilter.unclassified_no_flag,
    DensityFilter.noise_no_flag,
]

# Filters that expand to a group of other filters rather than producing a raster themselves.
DENSITY_FILTER_GROUPS: list[DensityFilter] = [
    DensityFilter.common,
    DensityFilter.common_no_flag,
    DensityFilter.all,
]

# Every filter that produces a raster, in the order they are declared.
DENSITY_FILTER_ALL: list[DensityFilter] = [
    f for f in DensityFilter if f not in DENSITY_FILTER_GROUPS
]

# || is OR and && is AND
# Class filters, each of which also has a "<name>_no_flag" version below.
DENSITY_FILTER_CLASS_WHERE: dict[DensityFilter, str] = {
    DensityFilter.ground: "(Classification == 2)",
    DensityFilter.low_veg: "(Classification == 3)",
    DensityFilter.medium_veg: "(Classification == 4)",
    DensityFilter.high_veg: "(Classification == 5)",
    DensityFilter.all_veg: "(Classification == 3 || Classification == 4 || Classification == 5)",
    DensityFilter.buildings: "(Classification == 6)",
    DensityFilter.unclassified: "(Classification == 1)",
    DensityFilter.noise: "(Classification == 7 || Classification == 18)",
    DensityFilter.water: "(Classification == 9)",
    DensityFilter.bridge: "(Classification == 17)",
}

# "No flag" means the same class with overlap and withheld points removed.
NO_FLAG_WHERE = "(Overlap == 0 && Withheld == 0)"

DENSITY_FILTER_WHERE_STATEMENTS: dict[DensityFilter, str | None] = {
    **DENSITY_FILTER_CLASS_WHERE,
    **{
        DensityFilter(f"{f.value}_no_flag"): f"({where} && {NO_FLAG_WHERE})"
        for f, where in DENSITY_FILTER_CLASS_WHERE.items()
    },
    DensityFilter.point: None,
    DensityFilter.withheld: "(Withheld == 1)",
    DensityFilter.overlap: "(Overlap == 1)",
    DensityFilter.noise_with_withheld: "((Classification == 7 || Classification == 18) && Withheld == 1)",
    DensityFilter.intensity: None,
    # First returns are closest to what the camera saw (the top surface).
    # Synthetic points (e.g. flattened water surfaces) are written with
    # ReturnNumber 0, so they are added explicitly or water tiles come out empty.
    DensityFilter.colourised: "((ReturnNumber == 1 || Synthetic == 1) && Withheld == 0)",
    # Pulse: first returns only, excluding status-flagged points.
    # Mirrors lasgrid: -first_only -drop_withheld -drop_synthetic -drop_keypoint
    # Overlap points are intentionally included to match ANPD aggregate behaviour.
    DensityFilter.pulse: "(ReturnNumber == 1 && Withheld == 0 && Synthetic == 0 && KeyPoint == 0)",
}


def create_all_rasters_per_tile_pdal(
    input_file: Path,
    output_dirs: dict[str, Path],
    filters: list[DensityFilter],
) -> None:
    """
    Process all requested density filters for a single tile in one PDAL pipeline.
    The LAZ file is read and decompressed once, with each filter written as a
    separate writers.gdal stage. This avoids redundant decompression when
    multiple density products are requested for the same tile.
    Bounds are explicitly set from the tile header so that tiles with zero
    points matching a filter still produce a valid output raster filled with
    nodata rather than raising a grid width error.
    Args:
        input_file: tile to process.
        output_dirs: mapping of filter value string to its output directory.
        filters: which filters to run for this tile.
    """
    # Read header bounds first using a metadata-only pipeline
    # This is fast — no point data is read
    header_pipeline = pdal.Pipeline(
        json.dumps(
            [
                {
                    "type": "readers.las",
                    "filename": str(input_file),
                    "count": 0,  # read header only, no points
                }
            ]
        )
    )
    header_pipeline.execute()
    header = header_pipeline.metadata["metadata"]["readers.las"]
    bounds = (
        f"([{header['minx']}, {header['maxx']}], [{header['miny']}, {header['maxy']}])"
    )
    pdrf = header.get("dataformat_id")

    # Colour filters are skipped for tiles whose point format has no colour.
    if pdrf not in COLOUR_PDRFS:
        skipped = [f for f in filters if f in DENSITY_FILTER_COLOUR]
        if skipped:
            logger.warning(
                f"{input_file.name} is PDRF {pdrf} with no colour, "
                f"skipping {[f.value for f in skipped]}"
            )
        filters = [f for f in filters if f not in DENSITY_FILTER_COLOUR]
        if not filters:
            return

    pipeline_spec: list[dict] = [
        {
            "type": "readers.las",
            "filename": str(input_file),
        }
    ]
    colour_band_files: list[Path] = []

    for filter_ in filters:
        output_file = output_dirs[filter_.value] / f"{input_file.stem}.tif"

        if filter_ == DensityFilter.colourised:
            # One mean raster per band, merged into a single multi-band tif after.
            bands = ["Red", "Green", "Blue"]
            if pdrf in NIR_PDRFS:
                bands.append("Infrared")
            tmp_dir = output_dirs[filter_.value] / "tmp"
            tmp_dir.mkdir(exist_ok=True)
            for band in bands:
                band_file = tmp_dir / f"{input_file.stem}_{band}.tif"
                colour_band_files.append(band_file)
                pipeline_spec.append(
                    {
                        "type": "writers.gdal",
                        "resolution": "1",
                        "binmode": True,
                        "data_type": "Float32",
                        "nodata": "-9999",
                        "dimension": band,
                        "output_type": "mean",
                        "filename": str(band_file),
                        "bounds": bounds,
                        "where": DENSITY_FILTER_WHERE_STATEMENTS[filter_],
                    }
                )
            continue

        if filter_ == DensityFilter.intensity:
            dimension = "Intensity"
            output_type = "mean"
        else:
            dimension = "Z"
            output_type = "count"

        writer: dict = {
            "type": "writers.gdal",
            "resolution": "1",
            # binmode: each cell uses only the points inside that 1 m cell.
            # Without it PDAL uses every point within a radius of the cell centre,
            # so neighbouring cells share points and counts come out about 3x too high.
            "binmode": True,
            "data_type": "Int32",
            "nodata": "-9999",
            "dimension": dimension,
            "output_type": output_type,
            "filename": str(output_file),
            "bounds": bounds,
        }

        where_statement = DENSITY_FILTER_WHERE_STATEMENTS[filter_]
        if where_statement is not None:
            writer["where"] = where_statement

        pipeline_spec.append(writer)

    pipeline = pdal.Pipeline(json.dumps(pipeline_spec))
    pipeline.execute()

    if colour_band_files:
        merge_colour_bands(
            band_files=colour_band_files,
            output_file=output_dirs[DensityFilter.colourised.value]
            / f"{input_file.stem}.tif",
        )


def read_pdrf(input_file: Path) -> int | None:
    """
    Returns the point data record format from the file header, without reading points.
    """
    pipeline = pdal.Pipeline(
        json.dumps([{"type": "readers.las", "filename": str(input_file), "count": 0}])
    )
    pipeline.execute()
    return pipeline.metadata["metadata"]["readers.las"].get("dataformat_id")


COLOUR_NODATA = -1


def merge_colour_bands(band_files: list[Path], output_file: Path) -> None:
    """
    Merges the per-band mean rasters into one multi-band tif (R, G, B and NIR
    when present), then deletes the per-band files.
    Colour is normalised to 0-255 so 8-bit and 16-bit tiles look the same
    side by side and share one QML style. A tile is treated as 16-bit when any
    RGB cell mean is above 255, as an 8-bit tile can never go above 255.
    """
    arrays = []
    for band_file in band_files:
        with rasterio.open(band_file) as src:
            arrays.append(src.read(1))
            # Every band uses the same points, so they share one valid mask.
            if len(arrays) == 1:
                profile = src.profile
                valid_mask = src.read_masks(1) > 0
    stack = np.stack(arrays)

    rgb_max = float(stack[:3, valid_mask].max()) if valid_mask.any() else 0.0
    if rgb_max > 255:
        stack = stack / 257  # 65535 / 255
    out = np.where(valid_mask, np.clip(np.rint(stack), 0, 255), COLOUR_NODATA)

    profile.update(
        driver="GTiff",
        count=len(band_files),
        dtype="int16",
        nodata=COLOUR_NODATA,
        compress="lzw",
    )
    with rasterio.open(output_file, "w", **profile) as dst:
        dst.write(out.astype(np.int16))
        for i, band_file in enumerate(band_files, start=1):
            dst.set_band_description(i, band_file.stem.rsplit("_", 1)[-1])

    for band_file in band_files:
        band_file.unlink(missing_ok=True)


def remove_gross_files(folder: Path) -> None:
    for file in list(folder.glob("*.tfw")):
        file.unlink()
    for file in list(folder.glob("*.kml")):
        file.unlink()
