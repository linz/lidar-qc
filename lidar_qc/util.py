import os
from pathlib import Path

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
    Rename a file
    """ 
    try:    
        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
            logger.debug(f'renamed: {old_file_path} -> {new_file_path}')
        else:
            logger.error(f'{old_file_path} does not exist')
    except Exception as err:
        logger.error(f'Error renaming file: {err}')