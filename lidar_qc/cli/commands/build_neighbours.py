from pathlib import Path
from typing import Annotated, Generator, List, Optional

import typer

from lidar_qc.cli.commands.build_vrt import build_vrt
from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.cli.validations import validate_filter_args
from lidar_qc.log import configure_logging
from lidar_qc.neighbours import create_raster_per_tile
from lidar_qc.parallel import run_in_parallel, write_errors_csv


def build_neighbours(
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
        callback=validate_filter_args,
    ),
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(
        default=None,
    ),
) -> None:
    logger = configure_logging(verbose, log_file)
    start_time = start_timer()
    for folder in input_dir:
        subfolder = Path(folder / f"{folder.stem}_raster")
        if subfolder.exists() == False:
            subfolder.mkdir(exist_ok=True, parents=True)
            files = list(folder.glob("*.tif"))
        else:
            if Path(subfolder / "vrt").exists():
                logger.info(f"vrt folder found, skipping {folder.stem} processing")
                continue
            else:
                subfolder_files = {f.name for f in (subfolder.glob("*.tif"))}
                folder_files = {f.name for f in (folder.glob("*.tif"))}
                folder_files_filtered = list(folder_files - subfolder_files)
                logger.info(
                    f"{len(subfolder_files)} raster files found in {subfolder}, processing {len(folder_files_filtered)}/{len(folder_files)} raster files."
                )
                files = [subfolder / f for f in folder_files_filtered]
        start_message = f"Creating neighbors raster now for {folder}..."
        pbar_unit = "tile"
        results, errors = run_in_parallel(
            func=create_raster_per_tile,
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
