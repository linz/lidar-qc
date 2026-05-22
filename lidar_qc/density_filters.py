import json
from enum import Enum
from pathlib import Path

import pdal

from lidar_qc.log import get_logger

logger = get_logger()


class DensityFilter(str, Enum):
    """
    Assigning commandline filter inputs to variables.
    """

    common = "common"
    common_no_flag = "common_no_flag"
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

DENSITY_FILTER_WHERE_STATEMENTS: dict[DensityFilter, str | None] = {
    # || is OR and && is AND
    DensityFilter.ground: "(Classification == 2)",
    DensityFilter.low_veg: "(Classification == 3)",
    DensityFilter.buildings: "(Classification == 6)",
    DensityFilter.unclassified: "(Classification == 1)",
    DensityFilter.noise: "(Classification == 7 || Classification == 18)",
    DensityFilter.point: None,
    DensityFilter.withheld: "(Withheld == 1)",
    DensityFilter.overlap: "(Overlap == 1)",
    DensityFilter.ground_no_flag: "(Classification == 2 && Overlap == 0)",
    DensityFilter.low_veg_no_flag: "(Classification == 3 && Overlap == 0)",
    DensityFilter.buildings_no_flag: "(Classification == 6 && Overlap == 0)",
    DensityFilter.unclassified_no_flag: "(Classification == 1 && Withheld == 0 && Overlap == 0)",
    DensityFilter.noise_no_flag: "((Classification == 7 || Classification == 18) && Withheld == 0)",
    DensityFilter.noise_with_withheld: "((Classification == 7 || Classification == 18) && Withheld == 1)",
    DensityFilter.all_veg: "(Classification == 3 || Classification == 4 || Classification == 5)",
    DensityFilter.medium_veg: "(Classification == 4)",
    DensityFilter.high_veg: "(Classification == 5)",
    DensityFilter.bridge: "(Classification == 17)",
    DensityFilter.intensity: None,
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

    pipeline_spec: list[dict] = [
        {
            "type": "readers.las",
            "filename": str(input_file),
        }
    ]

    for filter_ in filters:
        output_file = output_dirs[filter_.value] / f"{input_file.stem}.tif"

        if filter_ == DensityFilter.intensity:
            dimension = "Intensity"
            output_type = "mean"
        else:
            dimension = "Z"
            output_type = "count"

        writer: dict = {
            "type": "writers.gdal",
            "resolution": "1",
            "radius": "1",
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


def remove_gross_files(folder: Path) -> None:
    for file in list(folder.glob("*.tfw")):
        file.unlink()
    for file in list(folder.glob("*.kml")):
        file.unlink()
