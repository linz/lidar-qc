import json
import subprocess
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
}


def create_raster_per_tile_pdal(
    input_file: Path, output_dir: Path, where_statement: str | None, dimension: str, output_type: str
) -> None:
    """
    Process to create the density raster tiles with PDAL pipeline.
    Output file is a tif grid with resolution of 1, where each cell is populated by the count of corresponding points.
    The points are filtered based on the command line argument --filter.

    Args:
        input_file: file to run through the pipeline.
        output_dir: where the output density raster is created.
        where_statement: how the input file is filtered during the pipeline.
        This is defined at command line using --filter.
    """
    output_file: Path = output_dir / f"{input_file.stem}.tif"
    pipeline_spec = [
        {"type": "readers.las", "filename": str(input_file)},
        {
            "type": "writers.gdal",
            "resolution": "1",
            "radius": "1",
            "data_type": "Uint16",
            "nodata": "0",
            "dimension": dimension,
            "output_type": output_type,
            "filename": str(output_file),
        },
    ]
    if where_statement is not None:
        pipeline_spec[1]["where"] = where_statement
    pipeline_spec_json = json.dumps(pipeline_spec)
    pipeline = pdal.Pipeline(pipeline_spec_json)
    pipeline.execute()


def create_raster_per_tile_lastools(input_file: Path, output_dir: Path) -> None:
    """
    Process to create the density raster tiles with LAStools lasgrid.
    This method is only used to create the pulse density.
    Output file is a tif grid with resolution of 1, where each cell is populated by the density of first return points.

    Args:
        input_file: file to run through the process.
        output_dir: where the output density raster is created.
    """
    output_file: Path = output_dir / f"{input_file.stem}.tif"
    args: list[str] = [
        r"C:\LAStools\bin\lasgrid.exe",
        "-i",
        str(input_file),
        "-density",
        "-step",
        "1",
        "-nodata",
        "9999",
        "-o",
        str(output_file),
        "-first_only",
        # "-drop_overlap",
        "-drop_withheld",
        "-drop_synthetic",
        "-drop_keypoint",
        "-quiet",
    ]
    result = subprocess.run(args=args, capture_output=True, shell=True, encoding="utf-8", check=True)
    if result.stderr and not result.stderr.startswith('Please note that LAStools is not "free"'):
        raise RuntimeError(f"Subprocess Error: {result.stderr}")


def remove_gross_files(folder: Path) -> None:
    for file in list(folder.glob("*.tfw")):
        file.unlink()
    for file in list(folder.glob("*.kml")):
        file.unlink()
