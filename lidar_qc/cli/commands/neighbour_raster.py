from pathlib import Path
from typing import List, Optional

import typer

from lidar_qc.array_calculations import create_neighbour_from_tile
from lidar_qc.cli.commands.build_vrt import build_vrt
from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.cli.validations import validate_raster_folders, validate_script_progress
from lidar_qc.log import configure_logging
from lidar_qc.parallel import run_in_parallel, write_errors_csv


def neighbour_raster(
    input_dir: List[Path] = typer.Option(
        [],
        "--input",
        "-i",
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        readable=True,
        resolve_path=True,
        help="Path to Raster Directory, files can be only tif format.",
        callback=validate_raster_folders,
    ),
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(
        default=None,
    ),
) -> None:
    """
    Creates neighbour rasters for a collection of DEM or DSM files, to aid in finding spikes and dips.
    """
    logger = configure_logging(verbose, log_file)
    start_time = start_timer()
    for folder in input_dir:
        subfolder = Path(folder / f"neighbour_raster")
        files: list[Path] | None = validate_script_progress(
            input_files=list(folder.glob("*.tif")), output_dir=subfolder, item=folder.stem
        )
        if not files:
            continue
        start_message = f"Creating neighbors raster now for {folder.name}..."
        pbar_unit = "tile"
        results, errors = run_in_parallel(
            func=create_neighbour_from_tile,
            items=files,
            extra_kwargs={
                "output_dir": subfolder,
            },
            start_message=start_message,
            pbar_unit=pbar_unit,
        )
        if errors:
            error_file = subfolder / f"{folder.stem}_errors.csv"
            write_errors_csv(errors=errors, output_file=error_file)
            logger.error(
                f"{len(errors)} errors while creating {folder.stem} density rasters, writing errors to {error_file.name}"
            )
        if len([subfolder.glob("*.tif")]) == 0:
            logger.error(f"No {folder.stem} density raster files created, skipping building vrt")
        else:
            build_vrt(input_dir=[subfolder], verbose=verbose, log_file=log_file, logger_=logger, called_from_cli=False)
    end_timer(start_time)
