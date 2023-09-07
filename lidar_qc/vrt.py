import json
import subprocess
from pathlib import Path
from typing import Any, Generator, List

from lidar_qc.log import get_logger

logger = get_logger()


def child_vrt_filepaths(vrt_dir: Path, ras_dir: Path) -> dict[Any, Any]:
    """
    Receives the path for the vrt folder and raster (parent) directory.
    Organises the file paths in the raster directory into a dictionary,
    where the key is the child vrt path and name, and the value is a list of raster file paths (max 300).
    Returns the dictionary described above.
    """
    tifs = sorted(list(ras_dir.glob("*.tif")))
    child_vrts = {}
    child_vrt_name = 0
    increment_list = []
    for i in tifs:
        increment_list.append(i)
        if len(increment_list) == 300:
            child_vrt_name += 1
            for tif in increment_list:
                dict_key = str(child_vrt_name)
                if Path(vrt_dir, (dict_key + ".vrt")) not in child_vrts.keys():
                    child_vrts[Path(vrt_dir, (dict_key + ".vrt"))] = [Path(ras_dir, tif)]
                else:
                    child_vrts[Path(vrt_dir, (dict_key + ".vrt"))].append(Path(ras_dir, tif))
            increment_list = []
    # If there are less than 300 files, create 1 vrt file path key and assign the tif file paths as values.
    if len(increment_list) < 300:
        child_vrt_name += 1
        for tif in increment_list:
            dict_key = str(child_vrt_name)
            if Path(vrt_dir, (dict_key + ".vrt")) not in child_vrts.keys():
                child_vrts[Path(vrt_dir, (dict_key + ".vrt"))] = [Path(ras_dir, tif)]
            else:
                child_vrts[Path(vrt_dir, (dict_key + ".vrt"))].append(Path(ras_dir, tif))
    return child_vrts


def gdalinfo(file: Path):
    """
    Runs GDAL tool gdalinfo in a subprocess, using the received path to the input file.
    Raises an exception if subprocess isnt successful.
    Returns the completed process string formated as json.
    """
    gdalinfo_args = f"gdalinfo -stats -mm -json {file}"
    try:
        result = subprocess.run(args=gdalinfo_args, capture_output=True, shell=True, check=True, encoding="utf-8")
    except Exception as err:
        ...
        raise err
    subprocess_output = result.stdout
    return json.loads(subprocess_output)


def gdalbuildvrt(files_txt: Path, files: List, vrt: Path) -> None:
    """
    Runs GDAL tool gdalbuildvrt through subprocess.
    A local text file of filepaths is required for gdalbuildvrt command.
    This file is unlinked after process.
    Args:
        files_txt: path to local text file.
        files: list of files for vrt.
        vrt: child vrt file path.
    """
    with open(files_txt, "w", encoding="utf-8") as f:
        f.write("\n".join([str(file) for file in files]))
    gdalbuildvrt_args = [
        "gdalbuildvrt",
        "-resolution",
        "highest",
        "-a_srs",
        "EPSG:2193",
        "-allow_projection_difference",
        "-r",
        "nearest",
        "-input_file_list",
        str(files_txt),
        str(vrt),
    ]
    try:
        result = subprocess.run(args=gdalbuildvrt_args, capture_output=True, shell=True, encoding="utf-8", check=True)
        if result.stderr:
            print(f"Subprocess Error: {result.stderr}")
    except subprocess.CalledProcessError as process_error:
        print(f"CalledProcessError: {process_error}")
    except Exception as error:
        print(f"Syntax/Exception Error: {error}")
    Path(files_txt).unlink(missing_ok=True)


def gdaladdo(vrt: Path) -> None:
    """
    Runs GDAL tool gdaladdo in a subprocess, using the received path to the vrt file.
    Raises an exception if subprocess isnt successful.
    """
    gdaladdo_args = ["gdaladdo", "-r", "nearest", str(vrt), "2", "4", "8", "16"]
    try:
        result = subprocess.run(args=gdaladdo_args, capture_output=True, shell=True, encoding="utf-8", check=True)
        if result.stderr:
            print(f"Subprocess Error: {result.stderr}")
    except subprocess.CalledProcessError as process_error:
        print(f"CalledProcessError: {process_error}")
    except Exception as error:
        print(f"Syntax/Exception Error: {error}")


def remove_files(folder: Path, pattern: str) -> None:
    """
    Removes files in a specified folder that match the glob pattern.
    """
    if len(files := list(folder.glob(pattern))) > 0:
        for file in files:
            Path(Path(folder, file)).unlink()


def create_child_vrt(child_vrts: dict, vrt_dir: Path, ras_dir: Path) -> List[Any]:
    """
    Runs gdalbuildvrt function for all key, value pairs in child_vrt dictionary.
    Removes xml files in raster directory that are created during gdalbuildvrt processing.
    Returns list of created child vrts.
    """
    for vrt, files in child_vrts.items():
        # files_txt_path = Path(vrt_dir).joinpath(Path(vrt).stem + ".txt")
        gdalbuildvrt(files_txt=Path(vrt_dir).joinpath(Path(vrt).stem + ".txt"), files=files, vrt=vrt)
    remove_files(ras_dir, "*.xml")
    return list(vrt_dir.glob("*.vrt"))


def create_main_vrt(child_vrts: List[Path], vrt_dir: Path, ras_dir: Path) -> None:
    """
    Runs gdalbuildvrt function using a list of child vrts as input, if there are more than 1.
    Outputs a main vrt named after the raster directory.
    Additionally runs gdaladdo to create an overview of the main vrt.
    If there is only 1 child vrt, gdaladdo is run on this.
    """
    if len(child_vrts) > 1:
        gdalbuildvrt(
            files_txt=Path(vrt_dir, f"{ras_dir.stem}.txt"), files=child_vrts, vrt=Path(vrt_dir, f"{ras_dir.stem}.vrt")
        )
        remove_files(ras_dir, "*.xml")
        gdaladdo(vrt=Path(vrt_dir, f"{ras_dir.stem}.vrt"))
    elif len(child_vrts) == 1:
        gdaladdo(vrt=Path(child_vrts[0]).rename(Path(vrt_dir, f"{ras_dir.stem}.vrt")))
    else:
        logger.error(f"No child vrts found in {vrt_dir}, check is files in {ras_dir}")
