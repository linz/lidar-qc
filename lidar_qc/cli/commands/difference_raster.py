import shutil
from pathlib import Path
from typing import Optional

import typer

from lidar_qc.array_calculations import create_difference_raster
from lidar_qc.cli.commands.build_vrt import build_vrt
from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.cli.validations import validate_raster_folder, validate_script_progress
from lidar_qc.log import configure_logging
from lidar_qc.parallel import run_in_parallel, write_errors_csv


def difference_raster(
    dem_dir: Path = typer.Option(
        ...,
        "--dem",
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        readable=True,
        resolve_path=True,
        help="Path to DEM Raster Directory i.e. 02_DEM. Raster files must be in .tif format.",
        callback=validate_raster_folder,
    ),
    dsm_dir: Path = typer.Option(
        ...,
        "--dsm",
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        readable=True,
        resolve_path=True,
        help="Path to DSM Raster Directory i.e. 03_DSM. Raster files must be in .tif format.",
        callback=validate_raster_folder,
    ),
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(
        default=None,
    ),
) -> None:
    """
    Creates a difference raster for a collection of DEM and DSM files,
    to aid in finding areas were DEM pixels are higher than their DSM counterparts.
    """
    logger = configure_logging(verbose, log_file)
    start_time = start_timer()
    dem_files: dict[str, Path] = {file.stem[4:]: file for file in dem_dir.glob("*.tif")}
    dsm_files: dict[str, Path] = {file.stem[4:]: file for file in dsm_dir.glob("*.tif")}
    files: list[tuple[Path, Path]] = []
    for basename, dem_path in dem_files.items():
        try:
            if dsm_path := dsm_files[basename]:
                files.append((dem_path, dsm_path))
        except:
            logger.error(f"{dem_path.stem} did not correspond to any DSM file in {dsm_dir}, tile will not be processed.")
    subfolder = dem_dir / Path("difference_raster")
    subfolder.mkdir(exist_ok=True, parents=True)
    start_message = f"Creating differencing raster now for {len(files)}/{len(dem_files.keys())} DEM files..."
    pbar_unit = "tile"
    results, errors = run_in_parallel(
        func=create_difference_raster,
        items=files,
        extra_kwargs={
            "output_dir": subfolder,
        },
        start_message=start_message,
        pbar_unit=pbar_unit,
    )
    if errors:
        error_file = subfolder / f"difference_processing_errors.csv"
        write_errors_csv(errors=errors, output_file=error_file)
        logger.error(f"{len(errors)} errors while creating differencing rasters, writing errors to {error_file.name}")
    if len([subfolder.glob("*.tif")]) == 0:
        logger.error(f"No difference raster files created, skipping building vrt")
    else:
        build_vrt(input_dir=[subfolder], verbose=verbose, log_file=log_file, logger_=logger, called_from_cli=False)
        style_file = Path(__file__).parents[2] / f"layer_styles/difference_raster.qml"
        if style_file.exists():
            vrt_folder = subfolder / "vrt"
            shutil.copy(style_file, vrt_folder)
    end_timer(start_time)
