from logging import Logger
from pathlib import Path
from typing import List, Optional

import typer

from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.log import configure_logging
from lidar_qc.vrt import find_vrts, make_vrt_paths_relative


def repair_vrt(
    input_dir: List[Path] = typer.Option(
        ...,
        "--input",
        "-i",
        exists=True,
        file_okay=False,
        dir_okay=True,
        readable=True,
        resolve_path=True,
        help="Folder to search (recursively) for VRT files, e.g. the dataset's Raw folder."
        " Can pass multiple times.",
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Report what would change without writing any files."
    ),
    any_folder: bool = typer.Option(
        False,
        "--any-folder",
        help="Also repair VRTs that are not inside a 'vrt' folder (by default only build-vrt outputs are touched).",
    ),
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(default=None),
) -> None:
    """
    Repairs VRT source paths after a dataset has been moved to another drive, machine or OS.
    Rewrites tif / child VRT paths to be relative to the VRT file, so the VRT opens wherever the folder lives.
    Expects the build-vrt layout: tifs in the raster folder, VRTs in a 'vrt' subfolder.
    """
    logger: Logger = configure_logging(verbose, log_file)
    start_time = start_timer()
    fixed_files = ok_files = problem_files = 0
    for root in input_dir:
        vrts = find_vrts(root, any_folder=any_folder)
        if not vrts:
            logger.warning(f"No VRT files found in {root}")
            continue
        logger.info(f"Checking {len(vrts)} VRT files in {root}...")
        for vrt in vrts:
            try:
                result = make_vrt_paths_relative(vrt, dry_run=dry_run)
            except Exception as error:  # malformed XML, permission denied, file locked, etc.
                logger.error(f"Could not process {vrt}: {error}")
                problem_files += 1
                continue
            if result.changed:
                fixed_files += 1
                action = "Would fix" if dry_run else "Fixed"
                logger.debug(f"{action} {result.fixed} source path(s) in {vrt}")
            else:
                ok_files += 1
                logger.debug(f"Already OK: {vrt}")
            if result.unresolved:
                problem_files += 1
                for message in result.unresolved[:5]:
                    logger.warning(f"{vrt}: {message}")
                if len(result.unresolved) > 5:
                    logger.warning(f"{vrt}: ...and {len(result.unresolved) - 5} more unresolved sources")
    verb = "would be fixed" if dry_run else "fixed"
    logger.info(
        f"VRT repair complete: {fixed_files} {verb}, {ok_files} already OK, {problem_files} with unresolved sources"
    )
    if fixed_files and not verbose:
        logger.info("Use --verbose to list each VRT.")
    end_timer(start_time)
