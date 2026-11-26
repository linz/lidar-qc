import shutil
from pathlib import Path
from typing import List, Optional

import typer

from lidar_qc.cli.commands.build_vrt import build_vrt
from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.cli.validations import validate_filter_args
from lidar_qc.density_filters import (
    COLOUR_PDRFS,
    DENSITY_FILTER_COLOUR,
    NIR_PDRFS,
    DensityFilter,
    create_all_rasters_per_tile_pdal,
    read_pdrf,
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
        [],
        "--filter",
        "-f",
        help="How the points will be filtered for the density raster",
        callback=validate_filter_args,
    ),
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(
        default=None,
    ),
) -> None:
    """
    Creates density rasters for a collection of point cloud files, to aid in finding data voids.
    The common density outputs are pulse, ground, noise, low vegetation, building, and unclassified rasters.
    Each tile is read once and all requested filters are written in a single PDAL pipeline.
    """
    logger = configure_logging(verbose, log_file)
    start_time = start_timer()

    all_input_files: list[Path] = list(input_dir.glob("*.la[sz]"))

    # validate_filter_args returns strings, so convert back to enums before use.
    active_filters: list[DensityFilter] = [DensityFilter(f) for f in density_filter]

    # Build output dirs and create them upfront
    output_dirs: dict[str, Path] = {}
    for filter_ in active_filters:
        subfolder = input_dir / f"{filter_.value}_raster"
        subfolder.mkdir(exist_ok=True)
        output_dirs[filter_.value] = subfolder

    # Colour filters only work on point formats with RGB. Check one tile's header
    # so a dataset without colour skips them once, rather than per tile every run.
    colour_filters = [f for f in active_filters if f in DENSITY_FILTER_COLOUR]
    dataset_has_nir = False
    if colour_filters and all_input_files:
        pdrf = read_pdrf(all_input_files[0])
        dataset_has_nir = pdrf in NIR_PDRFS
        if pdrf not in COLOUR_PDRFS:
            logger.warning(
                f"Point data format {pdrf} has no RGB, skipping "
                f"{[f.value for f in colour_filters]}"
            )
            active_filters = [f for f in active_filters if f not in colour_filters]
            for f in colour_filters:
                folder = output_dirs.pop(f.value)
                if not any(folder.iterdir()):
                    folder.rmdir()
            if not active_filters:
                end_timer(start_time)
                return

    # Skip tiles where all outputs already exist
    files_to_process: list[Path] = []
    skipped = 0
    for tile in all_input_files:
        all_exist = all(
            (output_dirs[f.value] / f"{tile.stem}.tif").exists() for f in active_filters
        )
        if all_exist:
            skipped += 1
        else:
            files_to_process.append(tile)

    if skipped:
        logger.info(f"Skipping {skipped} tiles where all outputs already exist")
    if not files_to_process:
        logger.info("All tiles already processed")
        end_timer(start_time)
        return

    logger.info(
        f"Processing {len(files_to_process)} tiles for filters: {[f.value for f in active_filters]}"
    )

    results, errors = run_in_parallel(
        func=create_all_rasters_per_tile_pdal,
        items=files_to_process,
        extra_kwargs={
            "output_dirs": output_dirs,
            "filters": active_filters,
        },
        start_message="Creating density rasters now...",
        pbar_unit="tile",
    )

    if errors:
        for filter_ in active_filters:
            error_file = output_dirs[filter_.value] / f"{filter_.value}_errors.csv"
            filter_errors = errors  # all errors are tile-level, not filter-level
            write_errors_csv(errors=filter_errors, output_file=error_file)
        logger.error(
            f"{len(errors)} tile errors encountered, see error CSVs in output directories"
        )

    # Build VRTs per filter
    for filter_ in active_filters:
        subfolder = output_dirs[filter_.value]
        if not any(subfolder.glob("*.tif")):
            logger.error(
                f"No {filter_.value} density raster files created, skipping building vrt"
            )
            continue
        build_vrt(
            input_dir=[subfolder],
            verbose=verbose,
            log_file=log_file,
            logger_=logger,
            called_from_cli=False,
        )
        vrt_style_file = (
            Path(__file__).parents[2] / f"layer_styles/{filter_.value}_raster.qml"
        )
        if vrt_style_file.exists():
            shutil.copy(vrt_style_file, subfolder / "vrt")
        if filter_ == DensityFilter.colourised:
            # Per-band rasters are deleted after merging, leaving tmp empty.
            shutil.rmtree(subfolder / "tmp", ignore_errors=True)
            if dataset_has_nir:
                # Same raster, styled as false colour (NIR, Red, Green).
                shutil.copy(
                    vrt_style_file.with_name("colourised_false_colour_raster.qml"),
                    subfolder / "vrt",
                )

    end_timer(start_time)
