import subprocess
from pathlib import Path
from typing import Any, List, Optional

import typer

from lidar_qc.cli.commands.build_vrt import build_vrt
from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.cli.validations import find_data_subdirs, validate_output_gpkg
from lidar_qc.dataset_info.output import save_to_gpkg
from lidar_qc.dataset_info.point_cloud_file_info import PointCloudFileInfo
from lidar_qc.dataset_info.summaries import summarise_supplied_tile_index
from lidar_qc.log import configure_logging
from lidar_qc.parallel import run_in_parallel, write_errors_csv
from lidar_qc.util import is_point_cloud_dir


def check_dataset(
    input_dir: Path = typer.Option(
        ...,
        "--input",
        "-i",
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        readable=True,
        resolve_path=True,
        help=(
            "Path to 'Raw' Directory containing product folders "
            "i.e. 01_Classified_Point_Cloud, 02_DEM, 03_DSM. "
            "Raster files must be .tif, point cloud files .las or .laz."
        ),
    ),
    output_gpkg: Path = typer.Option(
        ...,
        "--output",
        "-o",
        resolve_path=True,
        file_okay=True,
        dir_okay=False,
        callback=validate_output_gpkg,
        help="Path to output geopackage. Must include name and extension.",
    ),
    tile_index: Optional[Path] = typer.Option(
        None,
        "--tile-index",
        "-t",
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Path to project tile index.",
    ),
    ras_folder: Optional[List[str]] = typer.Option(
        None,
        "--ras-folder",
        "-r",
        file_okay=False,
        dir_okay=True,
        help=("Folder name of a raster directory to process. Can pass multiple times."),
    ),
    pc_folder: Optional[List[str]] = typer.Option(
        None,
        "--pc-folder",
        "-p",
        file_okay=False,
        dir_okay=True,
        help=(
            "Folder name of a point cloud directory to process. "
            "Can pass multiple times."
        ),
    ),
    build_vrts: bool = typer.Option(
        False,
        help="Build Virtual Rasters for raster products.",
    ),
    repair: bool = typer.Option(
        False,
        "--repair",
        help=(
            "Rewrite all point cloud files in place using pdal translate "
            "before processing, correcting any header count mismatches."
        ),
    ),
    pdal_info: bool = typer.Option(
        False,
        "--pdal-info",
        help=(
            "Write pdal info JSON output to a 'pdal_info_reports' folder "
            "alongside each point cloud directory."
        ),
    ),
    _500_tile_index: Optional[List[Path]] = typer.Option(
        None,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Path to tile index if point cloud is tiled to 1:500k.",
    ),
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(default=None),
) -> None:
    """
    Gathers metadata from collections of raster and point cloud files,
    runs checks based on LINZ specifications, and outputs to a geopackage.
    """
    logger = configure_logging(verbose, log_file)
    start_time = start_timer()

    if ras_folder is None:
        ras_folder = []
    if pc_folder is None:
        pc_folder = []

    raw_data_dirs = find_data_subdirs(input_dir, ras_folder, pc_folder)
    product_infos = {}
    product_summaries = {}
    product_infos_errors = {}

    for raw_data_dir, cls in raw_data_dirs:
        files: list[Path] = list(raw_data_dir.glob(cls.glob_pattern))
        if not files:
            logger.error(
                f"No files matching {cls.glob_pattern} found in {raw_data_dir}"
            )
            continue

        # --- Repair pass (point cloud only, opt-in) ---
        if repair and is_point_cloud_dir(raw_data_dir.name):
            logger.info(
                f"Running pdal translate repair on {len(files)} files "
                f"in {raw_data_dir.name}..."
            )
            repair_errors = []
            for file in files:
                try:
                    PointCloudFileInfo.repair_file(file)
                except RuntimeError as e:
                    logger.error(str(e))
                    repair_errors.append(file)
            if repair_errors:
                logger.error(
                    f"{len(repair_errors)} files failed repair in "
                    f"{raw_data_dir.name}, they will still be processed."
                )

        # --- Build extra_kwargs ---
        extra_kwargs: dict[str, Any] = {"supplied_tile_index_file": tile_index}
        if is_point_cloud_dir(raw_data_dir.name):
            pdal_info_dir = raw_data_dir / "pdal_info_reports" if pdal_info else None
            extra_kwargs["pdal_info_dir"] = pdal_info_dir

        # --- Process files ---
        file_infos, file_info_errors = run_in_parallel(
            func=cls.from_file,
            items=files,
            extra_kwargs=extra_kwargs,
            start_message=f"Starting '{raw_data_dir.name}' processing...",
            pbar_unit="tile",
        )

        if file_infos:
            product_infos[raw_data_dir.name] = file_infos
            product_summary = cls.summarise_func(file_infos)
            product_summaries[raw_data_dir.name] = product_summary

        if file_info_errors:
            logger.error(
                f"{len(file_info_errors)} files failed to parse from "
                f"{len(files)} files in {raw_data_dir}"
            )
            product_infos_errors[raw_data_dir.name] = file_info_errors

    product_summaries["supplied_tile_index"] = summarise_supplied_tile_index(tile_index)
    save_to_gpkg(output_gpkg, product_infos, product_infos_errors, product_summaries)

    if build_vrts:
        raster_dirs = [
            raw_data_dir[0]
            for raw_data_dir in raw_data_dirs
            if "dem" in raw_data_dir[0].name.lower()
            or "dsm" in raw_data_dir[0].name.lower()
        ]
        build_vrt(
            input_dir=raster_dirs,
            verbose=verbose,
            log_file=log_file,
            logger_=logger,
            called_from_cli=False,
        )

    end_timer(start_time)
