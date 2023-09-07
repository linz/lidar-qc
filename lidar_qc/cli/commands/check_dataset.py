from pathlib import Path
from typing import Any, Generator, List, Optional

import typer

from lidar_qc.cli.commands.build_vrt import build_vrt
from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.cli.validations import find_data_subdirs, validate_output_gpkg
from lidar_qc.dataset_info.output import save_to_gpkg
from lidar_qc.dataset_info.summaries import summarise_supplied_tile_index
from lidar_qc.log import configure_logging
from lidar_qc.parallel import run_in_parallel
from lidar_qc.util import is_point_cloud_dir
from lidar_qc.vrt import child_vrt_filepaths, create_child_vrt, create_main_vrt


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
        help="Path to 'Raw' Directory, the directory which contains product folders i.e. 01_Classified_Point_Cloud, 02_DEM, 03_DSM. "
        "Raster files must be in .tif format, point cloud files can be in either .las or .laz formats.",
    ),
    output_gpkg: Path = typer.Option(
        ...,
        "--output",
        "-o",
        resolve_path=True,
        file_okay=True,
        dir_okay=False,
        callback=validate_output_gpkg,
        help="Path to output geopackage. Must include the name and extension of the geopackage.",
    ),
    tile_index: Optional[Path] = typer.Option(
        None,
        "--tile-index",
        "-t",
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Path to project tile index",
    ),
    ras_folder: Optional[List[str]] = typer.Option(
        None,
        "--ras-folder",
        "-r",
        file_okay=False,
        dir_okay=True,
        help="Folder name of a raster directory to process."
        " Can pass multiple times to process multiple raster directories, i.e. DEM and DSM.",
    ),
    pc_folder: Optional[List[str]] = typer.Option(
        None,
        "--pc-folder",
        "-p",
        file_okay=False,
        dir_okay=True,
        help="Folder name of a point cloud directory to process."
        " Can pass multiple times to process multiple point cloud directories, i.e. multiple types of point cloud.",
    ),
    build_vrts: bool = typer.Option(False, help="Build Virtual Rasters for raster products."),
    no_lasinfo_txt: bool = typer.Option(False, "--no-otxt", help="Write lasinfo output to text files."),
    _500_tile_index: Optional[List[Path]] = typer.Option(
        None,
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
        help="Path to tile index if point cloud is tiled to 1:500k",
    ),
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(
        default=None,
    ),
) -> None:
    """
    Gathers metadata information from collections of raster and point cloud files,
    runs checks based on LINZ specifications, and outputs results to a geopackage.
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
            logger.error(f"No files matching {cls.glob_pattern} found in {raw_data_dir}")
            continue
        extra_kwargs: dict[str, Any] = {"supplied_tile_index_file": tile_index}
        if is_point_cloud_dir(raw_data_dir.name):
            extra_kwargs["no_lasinfo_txt"] = no_lasinfo_txt
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
                f"{len(file_info_errors)} files were unable to be parsed from {len(files)} files matching {cls.glob_pattern} found in {raw_data_dir}"
            )
            product_infos_errors[raw_data_dir.name] = file_info_errors

    product_summaries["supplied_tile_index"] = summarise_supplied_tile_index(tile_index)
    save_to_gpkg(output_gpkg, product_infos, product_infos_errors, product_summaries)
    if build_vrts:
        raster_dirs = [
            raw_data_dir[0]
            for raw_data_dir in raw_data_dirs
            if "dem" in raw_data_dir[0].name.lower() or "dsm" in raw_data_dir[0].name.lower()
        ]
        build_vrt(input_dir=raster_dirs, verbose=verbose, log_file=log_file, logger_=logger, called_from_cli=False)
    end_timer(start_time)
