from logging import Logger
from pathlib import Path
from typing import Any, Optional

import typer

from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.cli.validations import validate_input_laz_dir
from lidar_qc.file_conversion import decompress_file
from lidar_qc.log import configure_logging
from lidar_qc.parallel import run_in_parallel, write_errors_csv


def decompress_laz(
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
        help="File path to point cloud directory for files to decompress from laz to las.",
        callback=validate_input_laz_dir,
    ),
    output_dir: Path = typer.Option(
        ...,
        "--output",
        "-o",
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        readable=True,
        resolve_path=True,
        help="Output folder location where files will be decompressed to.",
    ),
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(default=None),
    logger_=typer.Option(default=None, hidden=True),
) -> None:
    """
    Decompresses LAZ files to LAS using laszip.
    """
    if logger_ is None:
        logger: Logger = configure_logging(verbose, log_file)
    else:
        logger = logger_
    start_time = start_timer()
    logger.info(f"Decompressing files in {input_dir}...")
    extra_kwargs: dict[str, Any] = {"output_dir": output_dir}
    files = list(input_dir.glob("*.laz"))
    result, errors = run_in_parallel(
        func=decompress_file,
        items=files,
        extra_kwargs=extra_kwargs,
        start_message=f"Starting file processing...",
        pbar_unit="tile",
    )
    if errors:
        error_file = input_dir / f"decompress_processing_errors.csv"
        write_errors_csv(errors=errors, output_file=error_file)
        logger.error(f"{len(errors)} errors while decompressing laz files, writing errors to {error_file.name}")
    end_timer(start_time)  # type: ignore
