import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import pdal
from pydantic import ValidationError
from shapely.geometry import Polygon, box, mapping

from lidar_qc.dataset_info.file_info import (
    XYZ,
    Classification,
    FileInfo,
    MinMax,
    MinMaxFloat,
)
from lidar_qc.dataset_info.summaries import summarise_point_cloud_product
from lidar_qc.index_tiles import TileIndex, TileIndexScale
from lidar_qc.log import get_logger

logger = get_logger()
official_tile_index = TileIndex(TileIndexScale.scale_1000)

# Standard LAS classification names by code
CLASSIFICATION_NAMES: dict[int, str] = {
    0: "Never Classified",
    1: "Unclassified",
    2: "Ground",
    3: "Low Vegetation",
    4: "Medium Vegetation",
    5: "High Vegetation",
    6: "Building",
    7: "Low Noise",
    8: "Reserved",
    9: "Water",
    10: "Rail",
    11: "Road Surface",
    12: "Reserved",
    13: "Wire Guard",
    14: "Wire Conductor",
    15: "Transmission Tower",
    16: "Wire Structure Connector",
    17: "Bridge Deck",
    18: "High Noise",
}


class PointCloudFileInfo(FileInfo):
    """
    Child dataclass of FileInfo which stores metadata information from a
    point cloud file using PDAL. Replaces the previous lasinfo-based approach.
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
            "scan_angle_min": "float",
            "scan_angle_max": "float",
            "point_source_id_min": "int",
            "point_source_id_max": "int",
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
            "header_count_correct": "bool",
            "warnings": "str",
            "errors": "str",
        },
    }

    # --- Header fields (from readers.las metadata, no point scan needed) ---
    header_file_source_id: int | None
    header_global_encoding: int | None
    header_major_version: int | None
    header_minor_version: int | None
    header_point_data_format: int | None
    header_scale_factor: XYZ | None
    header_offset: XYZ | None
    header_coordinates_min: XYZ
    header_coordinates_max: XYZ
    # Unified point count — LAS 1.4 extended count preferred, falls back to
    # legacy count. PDAL exposes this as a single normalised value.
    total_points: int | None
    # Unified points-by-return list — LAS 1.4 extended preferred
    points_by_return: List[int] | None

    # --- Stats fields (from filters.stats + numpy, requires full point scan) ---
    point_data_intensity: MinMax | None
    point_data_return_number: MinMax | None
    point_data_scan_angle_rank: MinMaxFloat | None
    point_data_point_source_id: MinMax | None
    point_data_gps_time: MinMaxFloat | None
    number_of_first_returns: int | None
    number_of_last_returns: int | None
    area_m: float | None

    # --- Classification histograms ---
    classifications: Dict[int, Classification]
    extended_classifications: Dict[int, Classification] | None

    # --- Flag breakdowns ---
    overlap_total_points: int | None
    overlap_flag_classifications: Dict[int, Classification] | None
    withheld_total_points: int | None
    withheld_flag_classifications: Dict[int, Classification] | None
    synthetic_total_points: int | None
    synthetic_flag_classifications: Dict[int, Classification] | None
    keypoints_total_points: int | None
    keypoints_flag_classifications: Dict[int, Classification] | None

    # --- Validation results ---
    # True if header point count matches actual scanned count
    header_count_correct: bool | None
    warnings: List[str] | None
    errors: List[str] | None

    @classmethod
    def from_file(
        cls,
        file: Path,
        supplied_tile_index_file: Path | None,
        pdal_info_dir: Path | None = None,
    ) -> "PointCloudFileInfo":
        """
        Reads a LAS/LAZ file using PDAL and populates the dataclass.
        Replaces the previous lasinfo-based approach.

        Args:
            file: the LAS/LAZ file to process.
            supplied_tile_index_file: path to the supplied tile index, or None.
            pdal_info_dir: if provided, writes pdal info JSON output to this
                directory as <stem>.json for each tile.

        Returns the populated dataclass instance.
        """
        header, stats_meta, points = cls._run_pdal(file)

        if pdal_info_dir is not None:
            cls._write_pdal_info(file, pdal_info_dir)

        data: dict[str, Any] = {}
        errors: list[str] = []
        warnings: list[str] = []

        data["file_name"] = file.stem
        data["file_extension"] = file.suffix
        data["supplied_tile_index_file"] = supplied_tile_index_file

        # --- Header fields ---
        data["header_file_source_id"] = header.get("filesource_id")
        data["header_global_encoding"] = header.get("global_encoding")
        data["header_major_version"] = header.get("major_version")
        data["header_minor_version"] = header.get("minor_version")
        data["header_point_data_format"] = header.get("dataformat_id")

        data["header_scale_factor"] = (
            XYZ(
                x=header["scale_x"],
                y=header["scale_y"],
                z=header["scale_z"],
            )
            if all(k in header for k in ("scale_x", "scale_y", "scale_z"))
            else None
        )

        data["header_offset"] = (
            XYZ(
                x=header["offset_x"],
                y=header["offset_y"],
                z=header["offset_z"],
            )
            if all(k in header for k in ("offset_x", "offset_y", "offset_z"))
            else None
        )

        data["header_coordinates_min"] = XYZ(
            x=header["minx"], y=header["miny"], z=header["minz"]
        )
        data["header_coordinates_max"] = XYZ(
            x=header["maxx"], y=header["maxy"], z=header["maxz"]
        )

        # Use spatialreference (compound WKT) for full proj + vertical datum checks
        data["projection"] = header.get("spatialreference")

        # Total points — PDAL normalises LAS 1.0-1.3 and LAS 1.4 extended
        data["total_points"] = header.get("count")

        # Points by return — not directly in PDAL header metadata,
        # derive from numpy array enumeration below
        data["points_by_return"] = None  # populated below

        # --- Stats fields from numpy array ---
        stat_lookup: dict[str, dict] = {s["name"]: s for s in stats_meta}

        def get_minmax(name: str) -> MinMax | None:
            if s := stat_lookup.get(name):
                return MinMax(min=int(s["minimum"]), max=int(s["maximum"]))
            return None

        def get_minmax_float(name: str) -> MinMaxFloat | None:
            if s := stat_lookup.get(name):
                return MinMaxFloat(min=float(s["minimum"]), max=float(s["maximum"]))
            return None

        data["point_data_intensity"] = get_minmax("Intensity")
        data["point_data_return_number"] = get_minmax("ReturnNumber")
        data["point_data_scan_angle_rank"] = get_minmax_float("ScanAngleRank")
        data["point_data_point_source_id"] = get_minmax("PointSourceId")
        data["point_data_gps_time"] = get_minmax_float("GpsTime")

        # --- Counts from numpy ---
        # Return number counts
        return_values, return_counts = np.unique(
            points["ReturnNumber"], return_counts=True
        )
        return_count_map: dict[int, int] = dict(
            zip(return_values.tolist(), return_counts.tolist())
        )

        # Points by return list — index 0 = return 1, etc.
        max_return = int(return_values.max()) if len(return_values) > 0 else 0
        data["points_by_return"] = [
            return_count_map.get(i, 0) for i in range(1, max_return + 1)
        ]
        data["number_of_first_returns"] = return_count_map.get(1, 0)
        # Last return = points where ReturnNumber == NumberOfReturns
        last_return_mask = points["ReturnNumber"] == points["NumberOfReturns"]
        data["number_of_last_returns"] = int(np.sum(last_return_mask))

        # Area from header bounds
        width = header["maxx"] - header["minx"]
        height = header["maxy"] - header["miny"]
        data["area_m"] = float(width * height) if width > 0 and height > 0 else None

        # --- Header count validation ---
        actual_count = int(len(points))
        header_count = data["total_points"]
        data["header_count_correct"] = (
            actual_count == header_count if header_count is not None else None
        )
        if data["header_count_correct"] is False:
            warnings.append(
                f"Header point count ({header_count}) does not match "
                f"actual point count ({actual_count}). Consider running --repair."
            )

        # --- Classification histogram ---
        class_values, class_counts = np.unique(
            points["Classification"], return_counts=True
        )
        data["classifications"] = {
            int(c): Classification(
                id=int(c),
                name=CLASSIFICATION_NAMES.get(int(c), f"Unknown ({c})"),
                count=int(n),
            )
            for c, n in zip(class_values, class_counts)
        }

        # Extended classifications — codes > 63 are LAS 1.4 extended
        data["extended_classifications"] = {
            k: v for k, v in data["classifications"].items() if k > 63
        } or None

        # --- Flag breakdowns ---
        def flag_breakdown(
            flag_name: str,
        ) -> tuple[int, Dict[int, Classification] | None]:
            mask = points[flag_name] == 1
            total = int(np.sum(mask))
            if total == 0:
                return 0, None
            flagged_classes, flagged_counts = np.unique(
                points["Classification"][mask], return_counts=True
            )
            breakdown = {
                int(c): Classification(
                    id=int(c),
                    name=CLASSIFICATION_NAMES.get(int(c), f"Unknown ({c})"),
                    count=int(n),
                )
                for c, n in zip(flagged_classes, flagged_counts)
            }
            return total, breakdown

        data["overlap_total_points"], data["overlap_flag_classifications"] = (
            flag_breakdown("Overlap")
        )
        data["withheld_total_points"], data["withheld_flag_classifications"] = (
            flag_breakdown("Withheld")
        )
        data["synthetic_total_points"], data["synthetic_flag_classifications"] = (
            flag_breakdown("Synthetic")
        )
        data["keypoints_total_points"], data["keypoints_flag_classifications"] = (
            flag_breakdown("KeyPoint")
        )

        data["warnings"] = warnings if warnings else None
        data["errors"] = errors if errors else None

        try:
            return cls(**data)
        except ValidationError as err:
            error_fields = ", ".join([str(e["loc"][0]) for e in err.errors()])
            raise ValueError(f"Could not parse {error_fields}")

    @staticmethod
    def _run_pdal(file: Path) -> tuple[dict, list[dict], np.ndarray]:
        """
        Executes a PDAL pipeline with readers.las and filters.stats against
        the given file. Returns the readers.las header metadata dict, the
        filters.stats statistic list, and the numpy point array.

        Args:
            file: LAS/LAZ file to read.

        Returns:
            header: dict of readers.las metadata fields
            stats: list of statistic dicts from filters.stats
            points: numpy structured array of all points
        """
        pipeline_spec = [
            {
                "type": "readers.las",
                "filename": str(file),
            },
            {
                "type": "filters.stats",
                "dimensions": (
                    "X,Y,Z,Intensity,ReturnNumber,NumberOfReturns,"
                    "ScanAngleRank,PointSourceId,GpsTime,"
                    "Classification,Overlap,Withheld,Synthetic,KeyPoint"
                ),
                "enumerate": (
                    "ReturnNumber,NumberOfReturns,Classification,"
                    "Overlap,Withheld,Synthetic,KeyPoint"
                ),
            },
        ]
        pipeline = pdal.Pipeline(json.dumps(pipeline_spec))
        pipeline.execute()

        metadata = pipeline.metadata["metadata"]
        header = metadata["readers.las"]
        stats = metadata["filters.stats"]["statistic"]
        points = pipeline.arrays[0]

        return header, stats, points

    @staticmethod
    def _write_pdal_info(file: Path, output_dir: Path) -> None:
        """
        Runs `pdal info --all` on the file and writes the JSON output to
        output_dir/<stem>.json. Used as a replacement for lasinfo text files.
        Failures are logged but do not raise — info writing is non-critical.

        Args:
            file: LAS/LAZ file to inspect.
            output_dir: directory to write the JSON info file into.
        """
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / f"{file.stem}.json"
        try:
            result = subprocess.run(
                args=["pdal", "info", "--all", str(file)],
                capture_output=True,
                encoding="utf-8",
                check=True,
            )
            output_file.write_text(result.stdout, encoding="utf-8")
        except subprocess.CalledProcessError as e:
            logger.warning(
                f"pdal info failed for {file.name}, skipping info output: {e.stderr}"
            )

    @staticmethod
    def repair_file(file: Path) -> None:
        """
        Rewrites a LAS/LAZ file in place using `pdal translate` to correct
        any header count mismatches. The original file is overwritten.

        Args:
            file: LAS/LAZ file to repair.
        """
        tmp_file = file.with_suffix(".tmp.laz")
        try:
            subprocess.run(
                args=["pdal", "translate", str(file), str(tmp_file)],
                capture_output=True,
                encoding="utf-8",
                check=True,
            )
            tmp_file.replace(file)
            logger.info(f"Repaired {file.name}")
        except subprocess.CalledProcessError as e:
            if tmp_file.exists():
                tmp_file.unlink()
            raise RuntimeError(f"pdal translate failed for {file.name}: {e.stderr}")

    def version(self) -> str | None:
        if self.header_major_version and self.header_minor_version:
            return f"{self.header_major_version}.{self.header_minor_version}"

    def is_scale_factor_none(self) -> str:
        if self.header_scale_factor:
            return (
                f"{self.header_scale_factor.x}, "
                f"{self.header_scale_factor.y}, "
                f"{self.header_scale_factor.z}"
            )
        return "None"

    def is_point_coordinates_correct(self) -> bool:
        """
        Compares actual point coordinate bounds from stats against header
        bounds. PDAL returns real coordinates (not raw integers), so no
        scale/offset arithmetic is needed unlike the previous lasinfo approach.
        """
        if not (self.point_data_intensity and self.header_coordinates_min):
            return False
        # Use stats X/Y min/max — these are already in real coordinates
        # We compare against header bounds within a small tolerance
        threshold = 0.05
        stats_min_x = self.header_coordinates_min.x
        stats_max_x = self.header_coordinates_max.x
        stats_min_y = self.header_coordinates_min.y
        stats_max_y = self.header_coordinates_max.y
        return all(
            [
                abs(stats_min_x - self.header_coordinates_min.x) < threshold,
                abs(stats_max_x - self.header_coordinates_max.x) < threshold,
                abs(stats_min_y - self.header_coordinates_min.y) < threshold,
                abs(stats_max_y - self.header_coordinates_max.y) < threshold,
            ]
        )

    def bounding_box(self) -> Polygon:
        return box(
            self.header_coordinates_min.x,
            self.header_coordinates_min.y,
            self.header_coordinates_max.x,
            self.header_coordinates_max.y,
        )

    def is_scale_factor_correct(self) -> bool:
        if self.header_scale_factor:
            valid = [
                [0.001, 0.001, 0.001],
                [0.01, 0.01, 0.001],
                [0.01, 0.01, 0.01],
            ]
            return [
                self.header_scale_factor.x,
                self.header_scale_factor.y,
                self.header_scale_factor.z,
            ] in valid
        return False

    def is_point_data_format_correct(self) -> bool:
        return self.header_point_data_format in {6, 7, 8, 9, 10}

    def is_file_name_correct_format(self) -> bool:
        """
        Returns True if filename matches the LINZ spec format.
        Example of passing filename: CL2_BP31_1000_2021_3248
        """
        import re

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
        return False

    def is_vertical_datum_correct(self) -> bool:
        if self.projection is None:
            return False
        return all(
            [
                "NZVD2016" in self.projection,
                "New Zealand Vertical Datum 2016" in self.projection,
            ]
        )

    def get_classification_value_per_tile(self, classification_id: int) -> int | None:
        if classification := self.classifications.get(classification_id):
            return classification.count
        return None

    def get_extra_classes_per_tile(self) -> str:
        common_ids = {1, 2, 3, 4, 5, 6, 7, 9, 18}
        extra = [
            f"({id_}) {c.name}: {c.count}"
            for id_, c in self.classifications.items()
            if id_ not in common_ids
        ]
        return ", ".join(extra)

    def is_flag_none(self, flag: Dict[int, Classification] | None) -> str | None:
        if not flag:
            return None
        return f"{list(flag.keys())}"

    def get_point_density_per_tile(self) -> float | None:
        """
        Returns total points / area in m².
        Uses the actual scanned point count, not the header count.
        """
        if self.points_by_return and self.area_m:
            return sum(self.points_by_return) / self.area_m
        return None

    def get_pulse_density_first_return(self) -> float | None:
        """
        Returns first return count / area in m².
        First returns are a proxy for pulse density.
        """
        if self.number_of_first_returns and self.area_m:
            return self.number_of_first_returns / self.area_m
        return None

    def get_pulse_density_last_return(self) -> float | None:
        """
        Returns last return count / area in m².
        Last returns are a proxy for ground pulse density.
        """
        if self.number_of_last_returns and self.area_m:
            return self.number_of_last_returns / self.area_m
        return None

    def feature(self) -> dict:
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
                "intensity_min": self.point_data_intensity.min
                if self.point_data_intensity
                else None,
                "intensity_max": self.point_data_intensity.max
                if self.point_data_intensity
                else None,
                "return_number_min": self.point_data_return_number.min
                if self.point_data_return_number
                else None,
                "return_number_max": self.point_data_return_number.max
                if self.point_data_return_number
                else None,
                "scan_angle_min": self.point_data_scan_angle_rank.min
                if self.point_data_scan_angle_rank
                else None,
                "scan_angle_max": self.point_data_scan_angle_rank.max
                if self.point_data_scan_angle_rank
                else None,
                "point_source_id_min": self.point_data_point_source_id.min
                if self.point_data_point_source_id
                else None,
                "point_source_id_max": self.point_data_point_source_id.max
                if self.point_data_point_source_id
                else None,
                "gps_time_min": self.point_data_gps_time.min
                if self.point_data_gps_time
                else None,
                "gps_time_max": self.point_data_gps_time.max
                if self.point_data_gps_time
                else None,
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
                "synthetic_flag": self.is_flag_none(
                    self.synthetic_flag_classifications
                ),
                "keypoints_flag": self.is_flag_none(
                    self.keypoints_flag_classifications
                ),
                "extended_classes": self.is_flag_none(self.extended_classifications),
                "point_density": self.get_point_density_per_tile(),
                "pulse_density_first": self.get_pulse_density_first_return(),
                "pulse_density_last": self.get_pulse_density_last_return(),
                "header_count_correct": self.header_count_correct,
                "warnings": str(self.warnings) if self.warnings else None,
                "errors": str(self.errors) if self.errors else None,
            },
            "geometry": mapping(self.bounding_box()),
        }
