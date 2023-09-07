from logging import Logger
from pathlib import Path
from typing import Annotated, List, Optional

import typer

from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.log import configure_logging
from lidar_qc.vrt import (
    child_vrt_filepaths,
    create_child_vrt,
    create_main_vrt,
    gdalinfo,
)


def build_vrt(
    input_dir: List[Path] = typer.Option(
        ...,
        "--input",
        "-i",
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        readable=True,
        resolve_path=True,
        help="File path to raster directory for files used to create vrt."
        " Can pass multiple times to process multiple raster directories, i.e. DEM and DSM.",
    ),
    stats: bool = False,
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(default=None),
    logger_=typer.Option(default=None, hidden=True),
    called_from_cli: Annotated[bool, typer.Option(hidden=True)] = True,
) -> None:
    """
    Creates a Virtual Raster for a collection of raster files using gdalbuildvrt.
    """
    if logger_ is None:
        logger: Logger = configure_logging(verbose, log_file)
    else:
        logger = logger_
    if called_from_cli:
        start_time = start_timer()
    for ras_dir in input_dir:
        logger.info(f"Creating vrt for {ras_dir}...")
        vrt_dir = Path(ras_dir, "vrt")
        vrt_dir.mkdir(exist_ok=True)
        child_vrts = child_vrt_filepaths(vrt_dir, ras_dir)
        child_vrts_ = create_child_vrt(child_vrts, vrt_dir, ras_dir)
        create_main_vrt(child_vrts_, vrt_dir, ras_dir)
        if stats:
            output = gdalinfo(file=Path(vrt_dir, f"{ras_dir.name}.vrt"))
            if bands := output.get("bands")[0]:
                min_pixel_value = bands.get("computedMin")
                max_pixel_value = bands.get("computedMax")
                logger.info(f"{ras_dir.name}.vrt minimum-maximum pixel value: {min_pixel_value} - {max_pixel_value}")
    if called_from_cli:
        end_timer(start_time)  # type: ignore
