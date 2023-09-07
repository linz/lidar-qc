import json
from pathlib import Path
from subprocess import PIPE, Popen
from typing import Any, Dict, List, Set, Tuple

import fiona

from lidar_qc.log import get_logger

logger = get_logger()


def extract_psids_per_file(file: Path) -> Tuple[str, Any]:
    """
    Receives a point cloud file path and runs it through a pdal command in subprocess.
    PDAL command filters info based on PointSourceId dimension and provides Point Source IDs as a list.
    Output is captured in standard-out and uses json library to access the pointsource id list.
    Returns a tuple of the tile name and a list of point source ids.
    """
    tile = file.stem
    try:
        pdalinfo_command = f"pdal info --stats {file} --filters.stats.dimensions=PointSourceId --enumerate=PointSourceId"
        sp = Popen(pdalinfo_command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        communicate_tuple = sp.communicate()
        subprocess_output = communicate_tuple[0]
        subprocess_error = communicate_tuple[1].decode("utf-8")
        if len(subprocess_error) > 0:
            logger.error(f"pdal info sterr for file {file.stem}: {subprocess_error}")
            return tile, None
        json_format = json.loads(subprocess_output)
        point_source_id: List[int] = json_format.get("stats").get("statistic")[0].get("values")
        return tile, point_source_id
    except Exception as error:
        logger.error(f"pdal info subprocess error for file {file.stem}: {error}")
        return tile, None


def extract_flightline_id(flightline: Path, fid_field: str) -> Set:
    """
    Receives information from shapefile in user defined field.
    Args:
        flightline: path to flightline shapefile, from supplier.
        fid_field: name of field that contains flightline ID.
    Returns a set of the flight ids.
    """
    with fiona.open(flightline, "r") as shapefile:
        flightline_psid = set()
        for record in shapefile:
            flightline_psid.add(record["properties"][fid_field])
        return flightline_psid


def extract_psids_for_dataset(psid_info: Dict) -> Set:
    """
    Receives the point source ID information for all files.
    Returns a set of the point source ids from the point clouds.
    """
    dataset_psids = set()
    for psids in psid_info.values():
        if psids:
            dataset_psids.add(*psids)
    return dataset_psids


def compare_psid_to_flightline(flight_ids: Set, ps_ids: Set) -> Dict[str, Tuple[str, set]]:
    """
    Compares the flightline and point source ID's to find any ID's that are only in one set.
    Returns a dictionary of issues found during this check.
    """
    issues: Dict[str, Tuple[str, set]] = {}
    check_flightline = flight_ids - ps_ids
    check_psid = ps_ids - flight_ids
    if len(check_flightline) > 0:
        issues["Extra Flightlines"] = (
            f"There are more flightline id's than point source id's by {len(check_flightline)}",
            check_flightline,
        )
    if len(check_psid) > 0:
        issues["Extra psids"] = (f"There are more point source id's than flightline id's by {len(check_psid)}", check_psid)
    return issues


def save_to_textfile(text_file: Path, point_source_dict: Dict) -> None:
    """
    Opens the text file, as append, and writes a list of point source ID's per file for the whole dataset.
    """
    with open(text_file, "a", encoding="utf-8") as f:
        f.write(f"LAS Files: Point Source ID's\nNumber of Files: {len(point_source_dict)}\n\n")
        for tile, point_source_id in point_source_dict.items():
            f.write(f"{tile}: {point_source_id}\n")
