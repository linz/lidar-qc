import os
from pathlib import Path
import shutil

from lidar_qc.log import get_logger

logger = get_logger()


def is_point_cloud_dir(name: str) -> bool:
    """
    Receives folder path and returns True if point, laz, or las is in the folder name.
    """
    return "point" in name.lower() or "laz" in name.lower() or "las" in name.lower()


def is_raster_dir(name: str) -> bool:
    """
    Receives folder path and returns True if dem or dsm is in the folder name.
    """
    return "dem" in name.lower() or "dsm" in name.lower()


def rename_file(old_file_path: Path, new_file_path: Path) -> None:
    """
    Rename a file in place, or copy it if the destination directory differs.
    """
    try:
        if not old_file_path.exists():
            logger.error(f"{old_file_path} does not exist")
            return

        # Ensure destination directory exists
        new_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Same directory → rename
        if old_file_path.parent == new_file_path.parent:
            old_file_path.rename(new_file_path)
            logger.debug(f"Renamed: {old_file_path} -> {new_file_path}")

        # Different directory → copy
        else:
            shutil.copy2(old_file_path, new_file_path)
            logger.debug(f"Copied: {old_file_path} -> {new_file_path}")

    except Exception as err:
        logger.error(f"Error processing file: {err}")


RASTER_EXTENSIONS = frozenset({".tif", ".tiff"})


def find_files(folder: Path, extensions: frozenset[str]) -> list[Path]:
    """
    Returns files in folder whose final extension (case-insensitive) is in extensions.
    Matching on the final suffix skips sidecars such as .tif.aux.xml or .tif.ovr,
    which a glob like '*.tif*' would wrongly include.
    """
    return sorted(
        p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in extensions
    )


def get_first_file_extension(dir_path: Path) -> str:
    """
    Returns the extension of the first file found in the given directory.
    """
    for item in dir_path.iterdir():
        if item.is_file():
            return item.suffix  # includes the dot, e.g. '.txt'
    return None
