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
    if not value.parent.exists() or not value.parent.is_dir():
        raise typer.BadParameter("File must be in a folder that exists")
    if not os.access(value.parent, os.W_OK):
        raise typer.BadParameter("File must be in a folder that is writable")
    return value


def validate_output_gpkg(value: Path) -> Path:
    if value.suffix != ".gpkg":
        raise typer.BadParameter("File must end in .gpkg")
    validate_file_parent(value)
    return value


def validate_geospatial_format(value: Path) -> Union[Path, None]:
    if value:
        if value.suffix != ".gpkg" and value.suffix != ".shp":
            raise typer.BadParameter("File must end in .gpkg or .shp")
        validate_file_parent(value)
    return value


def validate_input_las_dir(folder: Path) -> Path:
    if len(list(folder.glob("*.la[sz]"))) == 0:
        raise typer.BadParameter("Input directory does not contain LAS or LAZ files")
    return folder


def validate_raster_files(folder: Path) -> Path:
    if len(list(folder.glob("*.tif"))) == 0:
        raise typer.BadParameter("Input directory does not contain tif files")
    return folder


def validate_attribute_field(layer: Path, attribute: str) -> bool:
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


def remove_invalid_files(files: set, folder: Path):
    files_filtered = files.copy()
    for file in files:
        filepath: Path = Path(str(folder / Path(file)) + ".tif")
        if filepath.stat().st_size > 0:
            if not Path(str(folder / Path(file)) + ".tfw").exists():
                filepath.unlink()
                files_filtered.remove(file)
        elif filepath.stat().st_size == 0:
            filepath.unlink()
            files_filtered.remove(file)
    return files_filtered


def validate_script_progress(
    folder: Path, subfolder: Path, item: str, ext_folder: str, ext_subfolder: str
) -> list[Path] | None:
    if subfolder.exists() == False:
        subfolder.mkdir(exist_ok=True, parents=True)
        return list(folder.glob(ext_folder))
    else:
        if Path(subfolder / "vrt").exists():
            logger.info(f"vrt folder found, skipping {item} processing")
        else:
            folder_files: dict[str, str] = {f.stem: f.suffix for f in (folder.glob(ext_folder))}
            subfolder_files: set[str] = {f.stem for f in (subfolder.glob(ext_subfolder))}
            if item == DensityFilter.pulse.value:
                subfolder_files = remove_invalid_files(files=subfolder_files, folder=subfolder)
            folder_files_filtered = list(set(folder_files.keys()) - subfolder_files)
            logger.info(
                f"{len(subfolder_files)} raster files found in {subfolder}, processing {len(folder_files_filtered)}/{len(folder_files.keys())} files in {folder}"
            )
            return [Path(str(folder / f) + str(folder_files[f])) for f in folder_files_filtered]
