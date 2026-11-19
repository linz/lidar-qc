import json
import os
import subprocess
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, List

from lidar_qc.log import get_logger

logger = get_logger()


def child_vrt_filepaths(vrt_dir: Path, ras_dir: Path) -> dict[Any, Any]:
    """
    Receives the path for the vrt folder and raster (parent) directory.
    Organises the file paths in the raster directory into a dictionary,
    where the key is the child vrt path and name, and the value is a list of raster file paths (max 300).
    Returns the dictionary described above.
    """
    tifs = sorted(
        {f for ext in ("*.tif", "*.tiff", "*.TIF", "*.TIFF") for f in ras_dir.glob(ext)}
    )
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
                    child_vrts[Path(vrt_dir, (dict_key + ".vrt"))] = [
                        Path(ras_dir, tif)
                    ]
                else:
                    child_vrts[Path(vrt_dir, (dict_key + ".vrt"))].append(
                        Path(ras_dir, tif)
                    )
            increment_list = []
    # If there are less than 300 files, create 1 vrt file path key and assign the tif file paths as values.
    if len(increment_list) < 300:
        child_vrt_name += 1
        for tif in increment_list:
            dict_key = str(child_vrt_name)
            if Path(vrt_dir, (dict_key + ".vrt")) not in child_vrts.keys():
                child_vrts[Path(vrt_dir, (dict_key + ".vrt"))] = [Path(ras_dir, tif)]
            else:
                child_vrts[Path(vrt_dir, (dict_key + ".vrt"))].append(
                    Path(ras_dir, tif)
                )
    return child_vrts


def gdalinfo(file: Path):
    """
    Runs GDAL tool gdalinfo in a subprocess, using the received path to the input file.
    Raises an exception if subprocess isnt successful.
    Returns the completed process string formatted as json.
    """
    gdalinfo_args = ["gdalinfo", "-stats", "-mm", "-json", str(file)]
    try:
        result = subprocess.run(
            args=gdalinfo_args,
            capture_output=True,
            shell=False,
            check=True,
            encoding="utf-8",
        )
    except Exception as err:
        raise err
    return json.loads(result.stdout)


def gdalbuildvrt(files_txt: Path, files: List, vrt: Path) -> None:
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
        result = subprocess.run(
            args=gdalbuildvrt_args,
            capture_output=True,
            shell=False,
            encoding="utf-8",
            check=True,
        )
        if result.stderr:
            logger.warning(f"gdalbuildvrt stderr: {result.stderr}")
    except subprocess.CalledProcessError as process_error:
        logger.error(f"gdalbuildvrt failed: {process_error}")
    except Exception as error:
        logger.error(f"gdalbuildvrt error: {error}")
    Path(files_txt).unlink(missing_ok=True)
    # gdalbuildvrt writes absolute paths for tifs outside the vrt folder; make them relative so the
    # dataset still opens after being moved to another drive, machine or OS.
    if Path(vrt).exists():
        result_ = make_vrt_paths_relative(Path(vrt))
        for message in result_.unresolved:
            logger.warning(f"{Path(vrt).name}: {message}")


def gdaladdo(vrt: Path) -> None:
    """
    Runs GDAL tool gdaladdo in a subprocess, using the received path to the vrt file.
    Raises an exception if subprocess isnt successful.
    """
    gdaladdo_args = ["gdaladdo", "-r", "nearest", str(vrt), "2", "4", "8", "16"]
    try:
        result = subprocess.run(
            args=gdaladdo_args,
            capture_output=True,
            shell=True,
            encoding="utf-8",
            check=True,
        )
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
        gdalbuildvrt(
            files_txt=Path(vrt_dir).joinpath(Path(vrt).stem + ".txt"),
            files=files,
            vrt=vrt,
        )
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
            files_txt=Path(vrt_dir, f"{ras_dir.stem}.txt"),
            files=child_vrts,
            vrt=Path(vrt_dir, f"{ras_dir.stem}.vrt"),
        )
        remove_files(ras_dir, "*.xml")
        gdaladdo(vrt=Path(vrt_dir, f"{ras_dir.stem}.vrt"))
    elif len(child_vrts) == 1:
        gdaladdo(vrt=Path(child_vrts[0]).rename(Path(vrt_dir, f"{ras_dir.stem}.vrt")))
    else:
        logger.error(f"No child vrts found in {vrt_dir}, check is files in {ras_dir}")


@dataclass
class VrtRepairResult:
    """Outcome of rewriting the source paths in one VRT."""

    vrt: Path
    fixed: int = 0
    ok: int = 0
    unresolved: List[str] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        return self.fixed > 0


def _source_name(path_text: str) -> str:
    """
    Returns the file name from a source path written on any OS.
    Handles both separators so a Windows path is read correctly on Linux and vice versa.
    """
    return path_text.replace("\\", "/").rstrip("/").split("/")[-1]


def _relative_posix(target: Path, start: Path) -> str:
    """Relative path from start to target, always with forward slashes (GDAL accepts these on every OS)."""
    return os.path.relpath(target, start).replace(os.sep, "/")


def make_vrt_paths_relative(vrt: Path, dry_run: bool = False) -> VrtRepairResult:
    """
    Rewrites every SourceFilename in a VRT to a path relative to the VRT file (relativeToVRT="1").

    Each source is looked up in this order:
      1. Already relative and the file exists next to the VRT -> left alone (separators normalised to "/").
      2. A file with the same name in the VRT's own folder (child VRTs referenced by a main VRT).
      3. A file with the same name one folder up (tifs, as laid out by build-vrt).
      4. The original absolute path, if it still exists (e.g. only the vrt folder was moved).
    Sources that can't be found, and GDAL virtual file system paths (/vsi...), are left untouched.
    The file is only written if something changed and dry_run is False.
    """
    result = VrtRepairResult(vrt=vrt)
    vrt_dir = vrt.parent
    tree = ET.parse(vrt)

    for elem in tree.getroot().iter("SourceFilename"):
        old_text = (elem.text or "").strip()
        if not old_text or old_text.startswith("/vsi"):
            result.ok += 1
            continue
        is_relative = elem.get("relativeToVRT") == "1"
        normalised = old_text.replace("\\", "/")

        if is_relative and (vrt_dir / normalised).exists():
            if normalised == old_text:
                result.ok += 1
            else:
                elem.text = normalised
                result.fixed += 1
            continue

        name = _source_name(old_text)
        candidates = [vrt_dir / name, vrt_dir.parent / name]
        if not is_relative:
            candidates.append(Path(old_text))
        found = next((c for c in candidates if c.is_file()), None)
        if found is None:
            result.unresolved.append(f"source not found: {old_text}")
            continue
        try:
            new_text = _relative_posix(found, vrt_dir)
        except ValueError:
            # Different drive / UNC share on Windows: no relative path exists, keep the working absolute path.
            result.unresolved.append(f"on a different drive, left absolute: {old_text}")
            continue
        if is_relative and new_text == old_text:
            result.ok += 1
            continue
        elem.text = new_text
        elem.set("relativeToVRT", "1")
        result.fixed += 1

    if result.changed and not dry_run:
        tmp = vrt.with_name(vrt.name + ".tmp")
        tree.write(tmp, encoding="UTF-8", xml_declaration=False)
        os.replace(tmp, vrt)
    return result


def find_vrts(root: Path, any_folder: bool = False) -> List[Path]:
    """
    Recursively finds .vrt files under root.
    By default only VRTs inside a folder named "vrt" (as created by build-vrt) are returned.
    """
    vrts = sorted(p for p in root.rglob("*") if p.suffix.lower() == ".vrt" and p.is_file())
    if any_folder:
        return vrts
    return [p for p in vrts if p.parent.name.lower() == "vrt"]
