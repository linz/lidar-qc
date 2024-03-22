import shutil
from pathlib import Path
from typing import Annotated, Generator, List, Optional

import typer

from lidar_qc.cli.commands.build_vrt import build_vrt
from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.cli.validations import validate_filter_args, validate_script_progress
from lidar_qc.density_filters import (
    DENSITY_FILTER_WHERE_STATEMENTS,
    DensityFilter,
    create_raster_per_tile_lastools,
    create_raster_per_tile_pdal,
    remove_gross_files,
)
from lidar_qc.log import configure_logging
from lidar_qc.parallel import run_in_parallel, write_errors_csv


def density_raster(
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
        help="Path to Point Cloud Directory, files can be in either .las or .laz formats.",
    ),
    density_filter: List[DensityFilter] = typer.Option(
        [], "--filter", "-f", help="How the points will be filtered for the density raster", callback=validate_filter_args
    ),
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(
        default=None,
    ),
) -> None:
    """
    Creates density rasters for a collection of point cloud files, to aid in finding data voids.
    The common density outputs are pulse, ground, noise, low vegetation, building, and unclassified rasters.
    """
    logger = configure_logging(verbose, log_file)
    start_time = start_timer()
    for filter_ in density_filter:
        subfolder = Path(input_dir / f"{filter_.value}_raster")
        files: list[Path] | None = validate_script_progress(
            input_files=list(input_dir.glob("*.la[sz]")), output_dir=subfolder, item=filter_.value
        )
        if not files:
            continue
        start_message = f"Creating {filter_.value} density rasters now..."
        pbar_unit = "tile"
        if filter_ == DensityFilter.pulse:
            results, errors = run_in_parallel(
                func=create_raster_per_tile_lastools,
                items=files,
                extra_kwargs={
                    "output_dir": subfolder,
                },
                start_message=start_message,
                pbar_unit=pbar_unit,
            )
            remove_gross_files(subfolder)
        elif filter_ == DensityFilter.intensity:
            results, errors = run_in_parallel(
                func=create_raster_per_tile_pdal,
                items=files,
                extra_kwargs={
                    "output_dir": subfolder,
                    "where_statement": DENSITY_FILTER_WHERE_STATEMENTS[filter_],
                    "dimension": "Intensity",
                    "output_type": "mean",
                },
                start_message=start_message,
                pbar_unit=pbar_unit,
            )
        else:
            results, errors = run_in_parallel(
                func=create_raster_per_tile_pdal,
                items=files,
                extra_kwargs={
                    "output_dir": subfolder,
                    "where_statement": DENSITY_FILTER_WHERE_STATEMENTS[filter_],
                    "dimension": "Z",
                    "output_type": "count",
                },
                start_message=start_message,
                pbar_unit=pbar_unit,
            )
        if errors:
            error_file = subfolder / f"{filter_.value}_errors.csv"
            write_errors_csv(errors=errors, output_file=error_file)
            logger.error(
                f"{len(errors)} errors while creating {filter_.value} density rasters, writing errors to {error_file.name}"
            )
        if len([subfolder.glob("*.tif")]) == 0:
            logger.error(f"No {filter_.value} density raster files created, skipping building vrt")
        else:
            build_vrt(input_dir=[subfolder], verbose=verbose, log_file=log_file, logger_=logger, called_from_cli=False)
            vrt_style_file = Path(__file__).parents[2] / f"layer_styles/{filter_.value}_raster.qml"
            if vrt_style_file.exists():
                vrt_folder = subfolder / "vrt"
                shutil.copy(vrt_style_file, vrt_folder)
    end_timer(start_time)

    """
    TO DO:
    - add variable to create where statement in commandline
    - add intensity where statement
    - Add docstrings to all new functions
    """
