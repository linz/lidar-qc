import os
from pathlib import Path
from typing import Annotated, Optional

import typer

from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.cli.validations import find_data_subdirs, validate_year
from lidar_qc.log import configure_logging
from lidar_qc.parallel import run_in_parallel
from lidar_qc.util import is_point_cloud_dir, is_raster_dir, rename_file


def rename(
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
        help="Path to directory containing subfolders of raster and point cloud files",
        show_default=False
    ),
    survey_start_year: str = typer.Option(None,"--year","-y", prompt_required=True,help="Start year of survey", callback=validate_year,show_default=False),
    write: Optional[bool] = typer.Option(
        None,
        "--write",
        "-w",
        file_okay=False,
        dir_okay=False,
        help="Confirm overwrite",
    ),
    limit: Optional[int] = typer.Option(
        None,
        "--limit",
        "-l",
        help="Limit the amount of files dry-run is run against. If not specified, there is no limit.",
        show_default=False
    ),
    stats: bool = False,
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(default=None),
    logger_=typer.Option(default=None, hidden=True),
    called_from_cli: Annotated[bool, typer.Option(hidden=True)] = True,
):
    """
    Rename a collection of files of either DEM, DSM or CL2.
    """

    # Make dry-run always verbose
    if not write:
        verbose = True

    if logger_ is None:
        logger: Logger = configure_logging(verbose, log_file)
    else:
        logger = logger_
    if called_from_cli:
        start_time = start_timer()


    if not write:
        logger.info('This is a dry-run, no files are being modified. To execute rename, use --write')

    # find raster and point cloud sub-directories
    raw_data_dirs = find_data_subdirs(input_dir,[],[])

    for raw_data_dir, cls in raw_data_dirs:
        # get all the files from the subdirectories which match glob_pattern
        files: list[Path] = list(raw_data_dir.glob(cls.glob_pattern))

        # apply limit for dry-run if specified
        if write is None and limit is not None: 
            files = files[:limit]

        file_infos = []

        extra_kwargs: dict[str, Any] = {"supplied_tile_index_file": None}
        if is_point_cloud_dir(raw_data_dir.name):
            extra_kwargs["no_lasinfo_txt"] = True
        
        file_infos, file_info_errors = run_in_parallel(
            func=cls.from_file,
            items=files,
            extra_kwargs=extra_kwargs,
            start_message=f"Renaming files in '{raw_data_dir.name}' ...",
            pbar_unit="tile",
        )

        if file_info_errors:
            logger.error(
                f"{len(file_info_errors)} files were unable to be parsed from {len(files)} files matching {cls.glob_pattern} found in {raw_data_dir}"
            )


        if file_infos:
            for file_info in file_infos:
                
                # Get the official tile for this file
                official_tile = file_info.get_correct_tile().feature_properties()

                # Define if this file type is Raster or Point Cloud, to help determine later which prefix and suffix to use
                product_type = file_info.product_type.value if file_info.file_type == 'Raster' else 'CL2' if file_info.file_type == 'PointCloud' else None

                # Build new file path
                current_file_path = os.path.join(raw_data_dir, file_info.file_name + file_info.file_extension)
                new_file_path = os.path.join(raw_data_dir, product_type + '_' + official_tile["sheet_code_id"] + '_' + survey_start_year + '_' + str(official_tile["scale"]) + '_' + official_tile["tile"] + file_info.file_extension)           
                
                
                # If raster, accomodate tfw files if they exist.
                tfw = False
                if file_info.file_type == 'Raster':
                    if os.path.exists(Path(current_file_path).with_suffix('.tfw')):
                        tfw = True
                        current_tfw_file = Path(current_file_path).with_suffix('.tfw')
                        new_tfw_file = Path(new_file_path).with_suffix('.tfw')
                        
                # Output file name change ito logger if this is a dry-run
                if not write:
                    logger.debug(f'{current_file_path} --> {new_file_path}')
                    if tfw:
                        logger.debug(f'{current_tfw_file} --> {new_tfw_file}')
                
                # Execute write
                if write:
                    rename_file(current_file_path,new_file_path)
                    if tfw:
                        rename_file(current_tfw_file,new_tfw_file)


    logger.info(f"Renaming complete")

