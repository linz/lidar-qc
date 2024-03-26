import sys
from pathlib import Path
from typing import Any, Generator, List, Optional, Tuple

import typer

from lidar_qc.cli.timer import end_timer, start_timer
from lidar_qc.cli.validations import (
    validate_attribute_field,
    validate_geospatial_format,
    validate_input_pc_dir,
)
from lidar_qc.log import configure_logging
from lidar_qc.parallel import run_in_parallel
from lidar_qc.point_source_ids import (
    compare_psid_to_flightline,
    extract_flightline_id,
    extract_psids_for_dataset,
    extract_psids_per_file,
    save_to_textfile,
)


def psid(
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
        callback=validate_input_pc_dir,
        help="Path to pointcloud directory. Must contain las or laz files.",
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
        help="Path to directory where text file will be created. This directory must exist prior to script running.",
    ),
    flightline: Optional[Path] = typer.Option(
        None,
        "--flightline",
        "-f",
        exists=True,
        file_okay=True,
        dir_okay=False,
        resolve_path=True,
        callback=validate_geospatial_format,
        help="Path to supplied flightlines file. Must include the name and extension of the file, either geopackage or shapefile.",
    ),
    fid_field: Optional[str] = typer.Option(
        None,
        "--fid-field",
        file_okay=False,
        dir_okay=False,
        help="Name of the attribute field that contains the flightline ID's that correlate to the point source ID's.",
    ),
    verbose: bool = False,
    log_file: Optional[Path] = typer.Option(
        default=None,
    ),
) -> None:
    """
    Finds list of point source ID's (psid) for a given point cloud file using PDAL command,
    and prints the list and file name to text file.
    If flightline and fid_field arguments are used, the psid and flightline id's will be compared.
    """
    logger = configure_logging(verbose, log_file)

    if flightline and not fid_field:
        logger.error(f"--fid-field not input in commandline.")
        sys.exit()
    elif fid_field and not flightline:
        logger.error(f"--flightline not input in commandline.")
        sys.exit()
    elif flightline and fid_field:
        if validate_attribute_field(flightline, fid_field) == False:
            logger.error(
                f"Flightline ID field error: \n{fid_field} not found in schema, check attribute fields for:\n{flightline}"
            )
            sys.exit()
    start_time = start_timer()
    psid_info = {}
    text_file = output_dir.joinpath("point_source_ids.txt")
    with open(text_file, "a", encoding="utf-8") as f:
        f.write(f"Point Source ID Check\n\n")
    files: Generator[Path, None, None] = input_dir.glob("*.la[sz]")
    psids_per_tile, psid_errors = run_in_parallel(
        func=extract_psids_per_file,
        items=files,
        extra_kwargs={},
        start_message="Extracting point source ID's now...",
        pbar_unit="tile",
    )
    for item in psids_per_tile:
        psid_info[item[0]] = item[1]
    if flightline and fid_field:
        fids = extract_flightline_id(flightline, fid_field)
        psids = extract_psids_for_dataset(psid_info)
        match_issues = compare_psid_to_flightline(fids, psids)
        if match_issues:
            logger.error(f"Flightline and point source ID's do not match. Check for info:\n{text_file}")
            with open(text_file, "a", encoding="utf-8") as f:
                for key, item in match_issues.items():
                    f.write(f"ERROR    {key}: {item[0]}\nID's: {item[1]}\n\n")
        else:
            logger.info(f"Flightline and point source ID's match")
            with open(text_file, "a", encoding="utf-8") as f:
                f.write("Point source ID's match Flightline ID's\n\n")
    save_to_textfile(text_file, psid_info)
    end_timer(start_time)
