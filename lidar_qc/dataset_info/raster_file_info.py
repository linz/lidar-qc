import re
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple, Union

from pydantic import ValidationError
from shapely.geometry import Polygon, box, mapping

from lidar_qc.dataset_info.file_info import *
from lidar_qc.dataset_info.summaries import summarise_raster_product
from lidar_qc.index_tiles import TileIndex, TileIndexScale
from lidar_qc.log import get_logger
from lidar_qc.vrt import gdalinfo

logger = get_logger()
official_tile_index = TileIndex(TileIndexScale.scale_1000)


class RasterProductType(Enum):
    dem = "DEM"
    dsm = "DSM"
    unknown = "unknown"


class RasterFileInfo(FileInfo):
    """
    Child dataclass of FileInfo which stores metadata information from a raster file by parsing the output of gdalinfo.
    Returns the dataclass instance for the file.
    """
    file_type = "Raster"
    glob_pattern = "*.tif"
    summarise_func = summarise_raster_product
    _schema = {
        "geometry": "Polygon",
        "properties": {
            "name": "str",
            "width": "float",
            "height": "float",
            "resolution_x": "float",
            "resolution_y": "float",
            "nodata": "float",
            "filetype": "str",
            "min_pixel_value": "float",
            "max_pixel_value": "float",
            "origin_x": "float",
            "origin_y": "float",
            "is_tiling_correct": "bool",
            "is_file_name_correct_format": "bool",
            "is_file_name_correct_tile": "bool",
            "is_projection_correct": "bool",
            "is_in_supplied_tile_index": "bool",
        },
    }
    product_type: RasterProductType
    file_size: XY
    origin: XY
    pixel_size: XY
    coordinates_upper_left: XY
    coordinates_lower_left: XY
    coordinates_lower_right: XY
    coordinates_upper_right: XY
    coordinates_centre: XY
    nodata: int | None
    data_type: str
    max_pixel_value: float
    min_pixel_value: float

    @classmethod
    def from_file(cls, file: Path, supplied_tile_index_file: Path | None) -> "RasterFileInfo":
        """
        This function runs gdalinfo in a subprocess and saves the result using standard out.
        The output is a series of dictionaries due to -json argument,
        therefore the dataclass is populated using the dict.get method.

        Args:
            cls: the class instance.
            file: the file for a given class instance.
            supplied_tile_index_file: path to the supplied tile index (not a layer object).

        Returns the dataclass for the file.
        """
        gdalinfo_output = gdalinfo(file)
        data: dict[str, Any] = {}
        data["file_name"] = file.stem
        data["file_extension"] = file.suffix
        data["supplied_tile_index_file"] = supplied_tile_index_file

        if size := gdalinfo_output.get("size"):
            data["file_size"] = XY(x=size[0], y=size[1])
        else:
            data["file_size"] = None

        if coordinate_system := gdalinfo_output.get("coordinateSystem"):
            data["projection"] = coordinate_system.get("wkt")
        else:
            data["projection"] = None

        if geotransform := gdalinfo_output.get("geoTransform"):
            data["origin"] = XY(x=geotransform[0], y=geotransform[3])
            data["pixel_size"] = XY(x=geotransform[1], y=geotransform[5])
        else:
            data["origin"] = None
            data["pixel_size"] = None

        if corner_coordinates := gdalinfo_output.get("cornerCoordinates"):
            data["coordinates_upper_left"] = XY(
                x=corner_coordinates.get("upperLeft")[0],
                y=corner_coordinates.get("upperLeft")[1],
            )
            data["coordinates_lower_left"] = XY(
                x=corner_coordinates.get("lowerLeft")[0],
                y=corner_coordinates.get("lowerLeft")[1],
            )
            data["coordinates_lower_right"] = XY(
                x=corner_coordinates.get("lowerRight")[0],
                y=corner_coordinates.get("lowerRight")[1],
            )
            data["coordinates_upper_right"] = XY(
                x=corner_coordinates.get("upperRight")[0],
                y=corner_coordinates.get("upperRight")[1],
            )
            data["coordinates_centre"] = XY(
                x=corner_coordinates.get("center")[0],
                y=corner_coordinates.get("center")[1],
            )
        else:
            data["coordinates_upper_left"] = None
            data["coordinates_lower_left"] = None
            data["coordinates_lower_right"] = None
            data["coordinates_upper_right"] = None
            data["coordinates_centre"] = None

        if bands := gdalinfo_output.get("bands")[0]:
            data["data_type"] = bands.get("type")
            data["min_pixel_value"] = bands.get("computedMin")
            data["max_pixel_value"] = bands.get("computedMax")
            data["nodata"] = bands.get("noDataValue")
        else:
            data["data_type"] = None
            data["min_pixel_value"] = None
            data["max_pixel_value"] = None
            data["nodata"] = None

        if "DEM" in file.parent.name.upper():
            data["product_type"] = RasterProductType.dem
        elif "DSM" in file.parent.name.upper():
            data["product_type"] = RasterProductType.dsm
        else:
            data["product_type"] = RasterProductType.unknown

        try:
            return cls(**data)
        except ValidationError as err:
            error_fields = "; ".join([f'field:{e["loc"][0]}, value:{e["input"]}, message:{e["msg"]}' for e in err.errors()])
            raise ValueError(error_fields)

    def bounding_box(self) -> Polygon:
        """
        Receives an instance of the class.
        Returns a polygon feature that's created using the x/y coordinate values
        of the pixel in the upper left and lower right.
        This feature is used to create the index for the pointcloud tiles.
        """
        return box(
            self.coordinates_upper_left.x,
            self.coordinates_lower_right.y,
            self.coordinates_lower_right.x,
            self.coordinates_upper_left.y,
        )
    
    def centroid(self):
        return self.bounding_box.centroid()

    def is_file_name_correct_format(self) -> bool:
        """
        Receives an instance of the class.
        Returns True if all elements are met, False if 1 or more is not (or if the iterable is empty).
        Two exceptions are captured if any parts dont met a type check;
        i.e. creating int of parts, or checking if parts is numeric. If raised, function returns False.
        Correct format: DEM_CB11_2021_1000_4233
        """
        if self.file_name is None:
            return False
        parts = self.file_name.split("_")
        if self.product_type == RasterProductType.dem:
            product_name_correct = parts[0] == RasterProductType.dem.value
        elif self.product_type == RasterProductType.dsm:
            product_name_correct = parts[0] == RasterProductType.dsm.value
        else:
            product_name_correct = parts[0] in {"DEM", "DSM"}
        try:
            return all(
                [
                    len(parts) == 5,
                    product_name_correct,
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

    def feature(self) -> Union[Dict[str, dict], None]:
        bounding_box = self.bounding_box()
        if bounding_box is None:
            logger.error(f"No bounding box information for {self.file_name}")
        else:
            return {
                "properties": {
                    "name": self.file_name,
                    "width": self.file_size.x,
                    "height": self.file_size.y,
                    "resolution_x": self.pixel_size.x,
                    "resolution_y": self.pixel_size.y,
                    "nodata": self.nodata,
                    "filetype": self.data_type,
                    "min_pixel_value": self.min_pixel_value,
                    "max_pixel_value": self.max_pixel_value,
                    "origin_x": self.origin.x,
                    "origin_y": self.origin.y,
                    "is_tiling_correct": self.is_tiled_correctly(),
                    "is_file_name_correct_format": self.is_file_name_correct_format(),
                    "is_file_name_correct_tile": self.is_file_name_correct_tile(),
                    "is_projection_correct": self.is_projection_correct_espg(),
                    "is_in_supplied_tile_index": self.is_in_supplied_tile_index(),
                },
                "geometry": mapping(bounding_box),
            }
