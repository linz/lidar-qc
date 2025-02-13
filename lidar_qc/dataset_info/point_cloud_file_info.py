import re
import subprocess
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple, Union

from pydantic import ValidationError
from shapely.geometry import Polygon, box, mapping

from lidar_qc.dataset_info.file_info import *
from lidar_qc.dataset_info.summaries import summarise_point_cloud_product
from lidar_qc.index_tiles import TileIndex, TileIndexScale
from lidar_qc.log import get_logger

logger = get_logger()
official_tile_index = TileIndex(TileIndexScale.scale_1000)


class PointCloudFileInfo(FileInfo):
    """
    Child dataclass of FileInfo which stores metadata information from a pointcloud file by parsing the output of lasinfo.
    Returns the dataclass instance for the file.
    """

    file_type = "PointCloud"
    glob_pattern = "*.la[sz]"
    summarise_func = summarise_point_cloud_product
    _schema = {
        "geometry": "Polygon",
        "properties": {
            "filename": "str",
            "file_source_id": "int",
            "encoding": "int",
            "las_version": "str",
            "point_data_format": "int",
            "scale_factor": "str",
            "header_min_x": "float",
            "header_max_x": "float",
            "header_min_y": "float",
            "header_max_y": "float",
            "header_min_z": "float",
            "header_max_z": "float",
            "point_coordinates_match_header": "bool",
            "intensity_min": "int",
            "intensity_max": "int",
            "return_number_min": "int",
            "return_number_max": "int",
            "scan_angle_min": "int",
            "scan_angle_max": "int",
            "point_source_id_min": "float",
            "point_source_id_max": "float",
            "gps_time_min": "float",
            "gps_time_max": "float",
            "is_tiling_correct": "bool",
            "is_file_name_correct_format": "bool",
            "is_file_name_correct_tile": "bool",
            "is_projection_correct": "bool",
            "is_vertical_datum_correct": "bool",
            "is_in_supplied_tile_index": "bool",
            "classifications": "str",
            "unclassified": "int",
            "ground": "int",
            "low_veg": "int",
            "med_veg": "int",
            "high_veg": "int",
            "building": "int",
            "low_noise": "int",
            "water": "int",
            "high_noise": "int",
            "other_classes": "str",
            "overlap_flag": "str",
            "withheld_flag": "str",
            "synthetic_flag": "str",
            "keypoints_flag": "str",
            "extended_classes": "str",
            "point_density": "float",
            "pulse_density_first": "float",
            "pulse_density_last": "float",
            "warnings": "str",
            "errors": "str",
        },
    }
    header_file_source_id: int | None
    header_global_encoding: int | None
    header_major_version: int | None
    header_minor_version: int | None
    header_size: int | None
    header_point_data_format: int | None
    header_point_data_record_length: int | None
    header_number_of_points: int | None
    header_number_of_points_by_return: List[int] | None
    header_scale_factor: XYZ | None
    header_offset: XYZ | None
    header_coordinates_min: XYZ
    header_coordinates_max: XYZ
    header_extended_number_of_points: int | None
    header_extended_number_of_points_by_return: List[int] | None
    point_data_x: MinMax
    point_data_y: MinMax
    point_data_z: MinMax
    point_data_intensity: MinMax
    point_data_return_number: MinMax
    point_data_scan_direction_flag: MinMax | None
    point_data_scan_angle_rank: MinMax
    point_data_point_source_id: MinMax
    point_data_gps_time: MinMaxFloat
    number_of_first_returns: float | None
    number_of_last_returns: float | None
    area_m: float | None
    point_density: Returns | None
    point_spacing: Returns | None
    is_points_header_correct: bool | None
    is_extended_points_header_correct: bool | None
    is_points_by_return_in_header_correct: bool | None
    is_extended_points_by_return_in_header_correct: bool | None
    pulses_by_number_of_returns: List[int] | None
    classifications: Dict[int, Classification]
    extended_classifications: Dict[int, Classification] | None
    overlap_total_points: int | None
    overlap_flag_classifications: Dict[int, Classification] | None
    withheld_total_points: int | None
    withheld_flag_classifications: Dict[int, Classification] | None
    synthetic_total_points: int | None
    synthetic_flag_classifications: Dict[int, Classification] | None
    keypoints_total_points: int | None
    keypoints_flag_classifications: Dict[int, Classification] | None
    warnings: List[str] | None
    errors: List[str] | None

    @classmethod
    def from_file(cls, file: Path, supplied_tile_index_file: Path, no_lasinfo_txt: bool) -> "PointCloudFileInfo":
        """
        This function runs the _run_lasinfo method to capture the contents of the lasinfo file.
        The dataclass is then populated using regex expressions to store information from the lasinfo contents.

        Args:
            cls: the class instance. ? check with Andrew
            file: the file for a given class instance.
            supplied_tile_index_file: path to the supplied tile index (not a layer object).

        Returns the dataclass for the file.
        """
        lasinfo_output = cls._run_lasinfo(file, no_lasinfo_txt)
        integer = r"(-?\d+)"  # a group containing an optional hyphen minus followed by 1 or more digits.
        decimal = r"(-?\d+\.?\d*)"  # a group containing an optional hyphen minus followed by 1 or more digits followed by an optional dot followed by 0 or more digits.

        data: dict[str, Any] = {}
        data["file_name"] = file.stem
        data["file_extension"] = file.suffix
        data["supplied_tile_index_file"] = supplied_tile_index_file

        # Each match is either returning something or None.
        match = re.search(rf"\s+file source ID:\s+{integer}", lasinfo_output)
        data["header_file_source_id"] = int(match.group(1)) if match else None

        match = re.search(rf"\s+global_encoding:\s+{integer}", lasinfo_output)
        data["header_global_encoding"] = int(match.group(1)) if match else None

        match = re.search(rf"\s+version major\.minor:\s+{integer}\.{integer}", lasinfo_output)
        data["header_major_version"] = int(match.group(1)) if match else None
        data["header_minor_version"] = int(match.group(2)) if match else None

        match = re.search(rf"\s+header size:\s+{integer}", lasinfo_output)
        data["header_size"] = int(match.group(1)) if match else None

        match = re.search(rf"\s+point data format:\s+{integer}", lasinfo_output)
        data["header_point_data_format"] = int(match.group(1)) if match else None

        match = re.search(rf"\s+point data record length:\s+{integer}", lasinfo_output)
        data["header_point_data_record_length"] = int(match.group(1)) if match else None

        match = re.search(rf"\s+number of point records:\s+{integer}", lasinfo_output)
        data["header_number_of_points"] = int(match.group(1)) if match else None

        match = re.search(
            rf"\s+number of points by return:\s+{integer} {integer} {integer} {integer} {integer}", lasinfo_output
        )
        data["header_number_of_points_by_return"] = [int(x) for x in match.groups()] if match else None

        match = re.search(rf"\s+scale factor x y z:\s+{decimal} {decimal} {decimal}", lasinfo_output)
        data["header_scale_factor"] = (
            XYZ(x=float(match.group(1)), y=float(match.group(2)), z=float(match.group(3))) if match else None
        )

        match = re.search(rf"\s+offset x y z:\s+{decimal} {decimal} {decimal}", lasinfo_output)
        data["header_offset"] = (
            XYZ(x=float(match.group(1)), y=float(match.group(2)), z=float(match.group(3))) if match else None
        )

        match = re.search(rf"\s+min x y z:\s+{decimal} {decimal} {decimal}", lasinfo_output)
        data["header_coordinates_min"] = (
            XYZ(x=float(match.group(1)), y=float(match.group(2)), z=float(match.group(3))) if match else None
        )

        match = re.search(rf"\s+max x y z:\s+{decimal} {decimal} {decimal}", lasinfo_output)
        data["header_coordinates_max"] = (
            XYZ(x=float(match.group(1)), y=float(match.group(2)), z=float(match.group(3))) if match else None
        )

        match = re.search(rf"\s+extended number of point records:\s+{integer}", lasinfo_output)
        data["header_extended_number_of_points"] = int(match.group(1)) if match else None

        match = re.search(
            rf"\s+extended number of points by return:\s+{integer} {integer} {integer} {integer} {integer} {integer} {integer} {integer} {integer} {integer}",
            lasinfo_output,
        )
        data["header_extended_number_of_points_by_return"] = [int(x) for x in match.groups()] if match else None

        match = re.search(r"\s+WKT OGC COORDINATE SYSTEM:\n\s+(.+)", lasinfo_output)
        data["projection"] = str(match.group(1)) if match else None

        match = re.search(
            r"reporting minimum and maximum for all LAS point record entries \.\.\.\n"
            rf"\s+X\s+{integer}\s+{integer}\n"
            rf"\s+Y\s+{integer}\s+{integer}\n"
            rf"\s+Z\s+{integer}\s+{integer}",
            lasinfo_output,
        )
        data["point_data_x"] = MinMax(min=int(match.group(1)), max=int(match.group(2))) if match else None
        data["point_data_y"] = MinMax(min=int(match.group(3)), max=int(match.group(4))) if match else None
        data["point_data_z"] = MinMax(min=int(match.group(5)), max=int(match.group(6))) if match else None

        match = re.search(rf"\s+intensity\s+{integer}\s+{integer}", lasinfo_output)
        data["point_data_intensity"] = MinMax(min=int(match.group(1)), max=int(match.group(2))) if match else None

        match = re.search(rf"\s+return_number\s+{integer}\s+{integer}", lasinfo_output)
        data["point_data_return_number"] = MinMax(min=int(match.group(1)), max=int(match.group(2))) if match else None

        match = re.search(rf"\s+scan_direction_flag\s+{integer}\s+{integer}", lasinfo_output)
        data["point_data_scan_direction_flag"] = MinMax(min=int(match.group(1)), max=int(match.group(2))) if match else None

        match = re.search(rf"\s+scan_angle_rank\s+{integer}\s+{integer}", lasinfo_output)
        data["point_data_scan_angle_rank"] = MinMax(min=int(match.group(1)), max=int(match.group(2))) if match else None

        match = re.search(rf"\s+point_source_ID\s+{integer}\s+{integer}", lasinfo_output)
        data["point_data_point_source_id"] = MinMax(min=int(match.group(1)), max=int(match.group(2))) if match else None

        match = re.search(rf"\s+gps_time\s+{decimal}\s+{decimal}", lasinfo_output)
        data["point_data_gps_time"] = MinMaxFloat(min=float(match.group(1)), max=float(match.group(2))) if match else None

        match = re.search(rf"number of first returns:\s+{integer}", lasinfo_output)
        data["number_of_first_returns"] = int(match.group(1)) if match else None

        match = re.search(rf"number of last returns:\s+{integer}", lasinfo_output)
        data["number_of_last_returns"] = int(match.group(1)) if match else None

        match = re.search(rf"covered area in square meters\/kilometers:\s+{integer}\/{decimal}", lasinfo_output)
        data["area_m"] = int(match.group(1)) if match else None

        match = re.search(rf"point density:\s+all returns\s+{decimal}\s+last only\s+{decimal}", lasinfo_output)
        data["point_density"] = Returns(all=float(match.group(1)), last=float(match.group(2))) if match else None

        match = re.search(rf"\s+spacing:\s+all returns\s+{decimal}\s+last only\s+{decimal}", lasinfo_output)
        data["point_spacing"] = Returns(all=float(match.group(1)), last=float(match.group(2))) if match else None

        match = re.search(r"number of point records in header is correct\.", lasinfo_output)
        data["is_points_header_correct"] = bool(match) if match else None

        match = re.search(r"extended number of point records in header is correct\.", lasinfo_output)
        data["is_extended_points_header_correct"] = bool(match) if match else None

        match = re.search(r"number of points by return in header is correct\.", lasinfo_output)
        data["is_points_by_return_in_header_correct"] = bool(match) if match else None

        match = re.search(r"extended number of points by return in header is correct\.", lasinfo_output)
        data["is_extended_points_by_return_in_header_correct"] = bool(match) if match else None

        match = re.search(
            rf"overview over extended number of returns of given pulse:\s+{integer} {integer} {integer} {integer} {integer} {integer} {integer} {integer} {integer} {integer}",
            lasinfo_output,
        )
        data["pulses_by_number_of_returns"] = [int(x) for x in match.groups()] if match else None

        def add_regex_to_dictionary(search_string: str, data_key: str, total_points: str | None = None):
            # nonlocal data
            match = re.search(search_string, lasinfo_output)
            match_text = match.group(1) if match else None
            if total_points:
                data[total_points] = int(match.group(2)) if match else None
            if match_text:
                results = re.findall(
                    r"(\d+(?:(?= of)|(?=  ))).*((?:(?<=are )|(?<=  ))\w+\s*\w*|Reserved for ASPRS Definition)\s+\((\d+)\)",
                    str(match_text),
                )
                data[data_key] = {int(r[2]): Classification(id=int(r[2]), name=str(r[1]), count=int(r[0])) for r in results}
            else:
                data[data_key] = None

        add_regex_to_dictionary(rf"histogram of classification of points:\n((?: +\d+\s+.+?\)\n)+)", "classifications")
        add_regex_to_dictionary(
            rf"(\s+\+->\s+flagged as extended overlap:\s+{integer}\n(?:\s*\+--->.+?\)\n)*)",
            "overlap_flag_classifications",
            "overlap_total_points",
        )
        add_regex_to_dictionary(
            rf"(\s+\+->\s+flagged as withheld:\s+{integer}\n(?:\s*\+--->.+?\)\n)*)",
            "withheld_flag_classifications",
            "withheld_total_points",
        )
        add_regex_to_dictionary(
            rf"(\s+\+->\s+flagged as synthetic:\s+{integer}\n(?:\s*\+--->.+?\)\n)*)",
            "synthetic_flag_classifications",
            "synthetic_total_points",
        )
        add_regex_to_dictionary(
            rf"(\s+\+->\s+flagged as keypoints:\s+{integer}\n(?:\s*\+--->.+?\)\n)*)",
            "keypoints_flag_classifications",
            "keypoints_total_points",
        )
        add_regex_to_dictionary(
            rf"(histogram of extended classification of points:\n(?:\s*.+?\)\n)*)", "extended_classifications"
        )

        for search_string, data_key in [("WARNING", "warnings"), ("ERROR", "errors")]:
            match = re.findall(rf"(?<={search_string}: ).+", lasinfo_output)
            if len(match) == 0:
                data[data_key] = None
            else:
                data[data_key] = match

        try:
            return cls(**data)
        except ValidationError as err:
            error_fields = ", ".join([str(e["loc"][0]) for e in err.errors()])
            raise ValueError(f"Could not parse {error_fields}")

    @staticmethod
    def _run_lasinfo(file: Path, no_lasinfo_txt: bool) -> str:
        """
        Receives a file as a path and runs a subprocess with the file to create a lasinfo text file.
        Returns the contents of the lasinfo file as a string.
        """
        lasinfo_args = ["C:\\LAStools\\bin\\lasinfo.exe", "-cd", "-repair_counters", "-i", str(file)]
        if no_lasinfo_txt is False:
            lasinfo_dir = file.parent / "las_info_reports"
            lasinfo_dir.mkdir(exist_ok=True)
            lasinfo_file = lasinfo_dir / f"{file.stem}.txt"
            lasinfo_args.extend(["-o", str(lasinfo_file)])
        else:
            lasinfo_args.append("-stdout")
        result = subprocess.run(args=lasinfo_args, capture_output=True, shell=True, check=True)
        if result.stderr:
            raise RuntimeError(result.stderr)
        if no_lasinfo_txt is False:
            return lasinfo_file.read_text()  # type: ignore
        else:
            return result.stdout.decode().replace("\r\n", "\n")

    def version(self) -> Union[str, None]:
        """
        Receives an instance of the class.
        Returns a string of the major and minor las version.
        """
        if self.header_major_version and self.header_minor_version:
            return f"{self.header_major_version}.{self.header_minor_version}"

    def is_scale_factor_none(self) -> str:
        if self.header_scale_factor:
            return f"{self.header_scale_factor.x}, {self.header_scale_factor.y}, {self.header_scale_factor.z}"
        else:
            return "None"

    def is_point_coordinates_correct(self) -> bool:
        """
        Receives an instance of the class.
        Calculates the point data min/max x and y coordinates using the scale factor and offset.
        Compares these values to the header min/max x and y coordinates.
        If the difference is within 0.001, then the function returns true.
        """
        if self.header_scale_factor and self.header_offset:
            point_min_x = (self.point_data_x.min * self.header_scale_factor.x) + self.header_offset.x
            point_max_x = (self.point_data_x.max * self.header_scale_factor.x) + self.header_offset.x
            point_min_y = (self.point_data_y.min * self.header_scale_factor.y) + self.header_offset.y
            point_max_y = (self.point_data_y.max * self.header_scale_factor.y) + self.header_offset.y
            threshold = 0.001
            return all(
                [
                    point_min_x - self.header_coordinates_min.x < threshold,
                    point_max_x - self.header_coordinates_max.x < threshold,
                    point_min_y - self.header_coordinates_min.y < threshold,
                    point_max_y - self.header_coordinates_max.y < threshold,
                ]
            )
        else:
            return False

    def bounding_box(self) -> Polygon:
        """
        Receives an instance of the class.
        Returns a polygon feature thats created using the header coordinate values.
        This feature is used to create the index for the pointcloud tiles.
        """
        return box(
            self.header_coordinates_min.x,
            self.header_coordinates_min.y,
            self.header_coordinates_max.x,
            self.header_coordinates_max.y,
        )

    def bounding_box_point_data(self) -> Polygon:
        """
        Receives an instance of the class.
        Returns a polygon feature thats created using the header coordinate values.
        This feature is used to create the index for the pointcloud tiles.
        """
        if self.header_scale_factor and self.header_offset:
            return box(
                (self.point_data_x.min * self.header_scale_factor.x) + self.header_offset.x,
                (self.point_data_y.min * self.header_scale_factor.y) + self.header_offset.y,
                (self.point_data_x.max * self.header_scale_factor.x) + self.header_offset.x,
                (self.point_data_y.max * self.header_scale_factor.y) + self.header_offset.y,
            )
        else:
            return self.bounding_box()

    def is_scale_factor_correct(self) -> bool:
        """
        Receives an instance of the class.
        Returns True if any of the three elements are met. Will return False if all three are not met or if the iterable is empty.
        """
        if self.header_scale_factor:
            return any(
                [
                    [self.header_scale_factor.x, self.header_scale_factor.y, self.header_scale_factor.z]
                    == [0.001, 0.001, 0.001],
                    [self.header_scale_factor.x, self.header_scale_factor.y, self.header_scale_factor.z]
                    == [0.01, 0.01, 0.001],
                    [self.header_scale_factor.x, self.header_scale_factor.y, self.header_scale_factor.z] == [0.01, 0.01, 0.01],
                ]
            )
        else:
            return False

    def is_point_data_format_correct(self) -> bool:
        """
        Receives an instance of the class.
        Returns True if the header point data format is 6, 7, 8, 9, or 10. Will return False if not.
        """
        options: set[int] = {6, 7, 8, 9, 10}
        if self.header_point_data_format in options:
            return True
        else:
            return False

    def is_file_name_correct_format(self) -> bool:
        """
        Receives an instance of the class.
        Returns True if all elements are met, False if 1 or more is not (or if the iterable is empty).
        Two exceptions are captured if any parts dont met a type check;
        i.e. creating int of parts, or checking if parts is numeric. If raised, function returns False.
        Example of filename that would pass: CL2_BP31_1000_2021_3248
        """
        if self.file_name:
            parts = self.file_name.split("_")
            try:
                return all(
                    [
                        len(parts) == 5,
                        parts[0] == "CL2",
                        re.match(r"[A-Z]{2}\d{2}", parts[1]),
                        parts[2].isnumeric(),
                        2000 < int(parts[2]) < 2100,
                        parts[3] == "1000",
                        parts[4].isnumeric(),
                        len(parts[4]) == 4,
                    ]
                )
            except (IndexError, ValueError):
                return False
        else:
            return False

    def get_classification_value_per_tile(self, classification_id: int) -> int | None:
        """
        Receives an instance of the class, and a class ID.
        Returns the number of points for a classification, if the class ID is in the classification dictionary.
        """
        if classification := self.classifications.get(classification_id, None):
            return classification.count

    def get_extra_classes_per_tile(self):
        """
        Receives an instance of the class.
        Returns the ID, classification name and number of points for a classification in a string,
        if the classification ID is not in the common IDs list.
        """
        common_ids = {1, 2, 3, 4, 5, 6, 7, 9, 18}
        extra_classifications = [
            f"({id_}) {classification.name}: {classification.count}"
            for id_, classification in self.classifications.items()
            if classification.id not in common_ids
        ]
        return ", ".join(extra_classifications)

    def is_vertical_datum_correct(self) -> bool:
        if self.projection is None:
            return False
        return all(
            [
                "NZVD2016" in self.projection,
                "New Zealand Vertical Datum 2016" in self.projection,
            ]
        )

    def is_flag_none(self, flag: Dict[int, Classification] | None) -> str | None:
        if not flag:
            return None
        else:
            return f"{list(flag.keys())}"

    def is_none(self, check: Any, true_return: Any, false_return: Any) -> Any:
        if check:
            return true_return
        else:
            return false_return

    def get_point_density_per_tile(self):
        """
        Receives an instance of the class.
        Returns a float value calculated by dividing the the number of points (sum of all points by return) by the area in metres.
        To sum the number of points, preferably uses the number of points by return but if this is None,
        it will use the extended number of points by return.
        """
        if not self.header_extended_number_of_points_by_return and self.header_number_of_points_by_return:
            if self.area_m:
                return sum(self.header_number_of_points_by_return) / self.area_m
        else:
            if self.area_m and self.header_extended_number_of_points_by_return:
                return sum(self.header_extended_number_of_points_by_return) / self.area_m

    def get_pulse_density_first_return(self):
        """
        Receives an instance of the class.
        Returns a float value calculated by dividing the number of first returns by the area in metres.
        The first returns are a proxy for the number of pulses emitted during capture, i.e. pulse density.
        """
        if self.number_of_first_returns and self.area_m:
            return self.number_of_first_returns / self.area_m

    def get_pulse_density_last_return(self):
        """
        Receives an instance of the class.
        Returns a float value calculated by dividing the number of last returns by the area in metres.
        The last returns are the last part of a pulse to return, which is inferred to be ground.
        They can also be a proxy for the pulse density.
        """
        if self.number_of_last_returns and self.area_m:
            return self.number_of_last_returns / self.area_m

    def feature(self):
        """
        Receives an instance of the class.
        Returns a feature, of geometry using the bounding box, with a dictionary of attributes (properties).
        """
        return {
            "properties": {
                "filename": self.file_name,
                "file_source_id": self.header_file_source_id,
                "encoding": self.header_global_encoding,
                "las_version": self.version(),
                "point_data_format": self.header_point_data_format,
                "scale_factor": self.is_scale_factor_none(),
                "header_min_x": self.header_coordinates_min.x,
                "header_max_x": self.header_coordinates_max.x,
                "header_min_y": self.header_coordinates_min.y,
                "header_max_y": self.header_coordinates_max.y,
                "header_min_z": self.header_coordinates_min.z,
                "header_max_z": self.header_coordinates_max.z,
                "point_coordinates_match_header": self.is_point_coordinates_correct(),
                "intensity_min": self.point_data_intensity.min,
                "intensity_max": self.point_data_intensity.max,
                "return_number_min": self.point_data_return_number.min,
                "return_number_max": self.point_data_return_number.max,
                "scan_angle_min": self.point_data_scan_angle_rank.min,
                "scan_angle_max": self.point_data_scan_angle_rank.max,
                "point_source_id_min": self.point_data_point_source_id.min,
                "point_source_id_max": self.point_data_point_source_id.max,
                "gps_time_min": self.point_data_gps_time.min,
                "gps_time_max": self.point_data_gps_time.max,
                "is_tiling_correct": self.is_tiled_correctly(),
                "is_file_name_correct_format": self.is_file_name_correct_format(),
                "is_file_name_correct_tile": self.is_file_name_correct_tile(),
                "is_projection_correct": self.is_projection_correct_espg(),
                "is_vertical_datum_correct": self.is_vertical_datum_correct(),
                "is_in_supplied_tile_index": self.is_in_supplied_tile_index(),
                "classifications": f"{sorted(self.classifications.keys())}",
                "unclassified": self.get_classification_value_per_tile(1),
                "ground": self.get_classification_value_per_tile(2),
                "low_veg": self.get_classification_value_per_tile(3),
                "med_veg": self.get_classification_value_per_tile(4),
                "high_veg": self.get_classification_value_per_tile(5),
                "building": self.get_classification_value_per_tile(6),
                "low_noise": self.get_classification_value_per_tile(7),
                "water": self.get_classification_value_per_tile(9),
                "high_noise": self.get_classification_value_per_tile(18),
                "other_classes": self.get_extra_classes_per_tile(),
                "overlap_flag": self.is_flag_none(self.overlap_flag_classifications),
                "withheld_flag": self.is_flag_none(self.withheld_flag_classifications),
                "synthetic_flag": self.is_flag_none(self.synthetic_flag_classifications),
                "keypoints_flag": self.is_flag_none(self.keypoints_flag_classifications),
                "extended_classes": self.is_flag_none(self.extended_classifications),
                "point_density": self.get_point_density_per_tile(),
                "pulse_density_first": self.get_pulse_density_first_return(),
                "pulse_density_last": self.get_pulse_density_last_return(),
                "warnings": self.is_none(check=self.warnings, true_return=str(self.warnings), false_return=None),
                "errors": self.is_none(check=self.errors, true_return=str(self.errors), false_return=None),
            },
            "geometry": mapping(self.bounding_box()),
        }
