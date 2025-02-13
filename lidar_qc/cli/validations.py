import os
from pathlib import Path
from re import sub
from typing import Any, Iterable, List, Tuple, Type, Union

import fiona
import typer

from lidar_qc.dataset_info.point_cloud_file_info import PointCloudFileInfo
from lidar_qc.dataset_info.raster_file_info import RasterFileInfo
from lidar_qc.density_filters import (
    DENSITY_FILTER_COMMON,
    DENSITY_FILTER_COMMON_NO_FLAG,
    DensityFilter,
)
from lidar_qc.log import get_logger
from lidar_qc.parallel import FatalError
from lidar_qc.util import is_point_cloud_dir, is_raster_dir

logger = get_logger()


def validate_file_parent(value: Path) -> Path:
    """
    Raise error if file is not in a writable folder that exists.
    """
    if not value.parent.exists() or not value.parent.is_dir():
        raise typer.BadParameter("File must be in a folder that exists")
    if not os.access(value.parent, os.W_OK):
        raise typer.BadParameter("File must be in a folder that is writable")
    return value


def validate_output_gpkg(value: Path) -> Path:
    """
    Raise error if file suffix is not ".gpkg".
    """
    if value.suffix != ".gpkg":
        raise typer.BadParameter("File must end in .gpkg")
    validate_file_parent(value)
    return value


def validate_geospatial_format(value: Path) -> Union[Path, None]:
    """
    Raise error if file suffix is not ".gpkg" or ".shp".
    """
    if value:
        if value.suffix != ".gpkg" and value.suffix != ".shp":
            raise typer.BadParameter("File must end in .gpkg or .shp")
        validate_file_parent(value)
    return value


def validate_input_pc_dir(folder: Path) -> Path:
    """
    Raise error if folder does not contain ".las" or ".laz" files.
    """
    if len(list(folder.glob("*.la[sz]"))) == 0:
        raise typer.BadParameter("Input directory does not contain LAS or LAZ files")
    return folder


def validate_raster_folders(folders: list[Path]) -> list[Path]:
    """
    Raise error if any folder within the list of raster folders does not contain ".tif" files.
    """
    for folder in folders:
        if len(list(folder.glob("*.tif"))) == 0:
            raise typer.BadParameter(f"Input directory {folder.name} does not contain tif files")
    return folders


def validate_raster_folder(folder: Path) -> Path:
    """
    Raise error if folder does not contain ".tif" files.
    """
    if len(list(folder.glob("*.tif"))) == 0:
        raise typer.BadParameter(f"Input directory {folder.name} does not contain tif files")
    return folder


def validate_attribute_field(layer: Path, attribute: str) -> bool:
    """
    Return True if attribute is in layer schema, False if it's not.
    """
    with fiona.open(layer, "r") as c:
        if schema := c.schema:
            if attribute in list((schema)["properties"].keys()):
                return True
            else:
                return False
        else:
            return False


def validate_filter_args(filter_args: list[DensityFilter]) -> list[str]:
    """
    Receives list of filters input in command line.
    Refines list if common and common_no_flag filters are used.
    Returns a list of all filters.
    """
    if DensityFilter.common in filter_args:
        filter_args.remove(DensityFilter.common)
        filter_args.extend(DENSITY_FILTER_COMMON)
    if DensityFilter.common_no_flag in filter_args:
        filter_args.remove(DensityFilter.common_no_flag)
        filter_args.extend(DENSITY_FILTER_COMMON_NO_FLAG)
    return [filter_arg.value for filter_arg in filter_args]


def find_data_subdirs(
    input_dir: Path, raster_folders_names: List[str], pc_folders_names: List[str]
) -> List[Tuple[Path, Union[Type[RasterFileInfo], Type[PointCloudFileInfo]]]]:
    """
    Find the subdirectories that should contain collections of raster and
    pointcloud folders, based on their naming convention.
    If any of the supplied subfolder names are not directories within the
    input directory, a FatalError exception will be raised.

    Args:
        input_dir: directory specified in command line.
        raster_folders_names: list of folder names of raster product specified in command line.
        pc_folders_names: list of folder names of pointcloud product specified in command line.

    Returns: List of tuples of subfolder path and the type of dataclass for the given subfolder.
    """
    raw_data_dirs = []
    # If specific subfolder names have been supplied through command line.
    if raster_folders_names or pc_folders_names:
        for folder_name, file_info_class in [
            *[(name, RasterFileInfo) for name in raster_folders_names],
            *[(name, PointCloudFileInfo) for name in pc_folders_names],
        ]:
            raw_data_dir: Path = input_dir / folder_name
            if not raw_data_dir.is_dir():
                raise FatalError(f"'{raw_data_dir}' is not a folder/directory")
            else:
                raw_data_dirs.append((raw_data_dir, file_info_class))
    # If no specific subfolder names were supplied at command line.
    else:
        for child in input_dir.iterdir():
            if child.is_dir():
                if is_raster_dir(child.name):
                    raw_data_dirs.append((child, RasterFileInfo))
                if is_point_cloud_dir(child.name):
                    raw_data_dirs.append((child, PointCloudFileInfo))
    return raw_data_dirs


def remove_invalid_files(files: Iterable[Path]) -> list[Path]:
    """
    Receives list of files to iterate through.
    If files have been processed correctly, add file path to new list.
    If files have been partially processed, delete files.
    Returns: List of files that have been processed correctly.
    """
    valid_files: list[Path] = []
    for file in files:
        if file.stat().st_size > 0:
            if not file.with_suffix(".tfw").exists():
                file.unlink()
            else:
                valid_files.append(file)
        elif file.stat().st_size == 0:
            file.unlink()
    return valid_files


def validate_script_progress(input_files: list[Path], output_dir: Path, item: str) -> list[Path]:
    """
    Receives list of input files, output directory path, and an item to indicate what is being processed.
    Code will look in subfolder to work out where its up to in the process:
        - has the subfolder been created? If not, at the start of the process.
          Return input file list.
        - subfolder exists, does the vrt folder exist? If it does, then all files have been processed.
          Return an empty list.
        - subfolder exists but vrt folder doesnt exist, therefore processing was stopped mid-way through.
          Return a filtered list of files still to be processed.
    """
    if not output_dir.exists():
        output_dir.mkdir(exist_ok=True)
        return input_files
    if Path(output_dir / "vrt").exists():
        logger.info(f"vrt folder found, skipping {item} processing")
        return []
    output_files = list(output_dir.glob("*.tif"))
    if item == DensityFilter.pulse.value:
        output_files: list[Path] = remove_invalid_files(files=output_files)
    folder_files_filtered: list[Path] = [f for f in input_files if f.stem not in {o_f.stem: o_f for o_f in output_files}]
    logger.info(
        f"{len(output_files)} raster files found in {output_dir}, processing {len(folder_files_filtered)}/{len(input_files)} files for {item}"
    )
    return folder_files_filtered

def validate_year(year_string: str) -> str:
    """
    Ensure the year that is inputted is a digit, not None and is four digits.
    """
    if year_string is not None and year_string.isdigit() and len(year_string) == 4:
        return year_string
    else:
        raise typer.BadParameter(f"Year {year_string} is not valid")
