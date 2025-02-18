from pathlib import Path
from typing import ClassVar, Dict, NamedTuple

import fiona
import fiona.collection
import shapely
from pydantic import BaseModel
from shapely.geometry import Polygon, shape
from shapely.strtree import STRtree

from lidar_qc.index_tiles import TileIndex, TileIndexScale
from lidar_qc.log import get_logger

official_tile_index = TileIndex(TileIndexScale.scale_1000)
logger = get_logger()


_strtrees: Dict[Path, STRtree] = {}


class MinMax(NamedTuple):
    min: int
    max: int


class MinMaxFloat(NamedTuple):
    min: float
    max: float


class XYZ(NamedTuple):
    x: float
    y: float
    z: float


class Classification(NamedTuple):
    id: int
    name: str
    count: int


class XY(NamedTuple):
    x: float
    y: float


class Returns(NamedTuple):
    all: float
    last: float


class FileInfo(BaseModel):
    """
    Parent dataclass created using BaseModel from pydantic.
    Contains class methods which pertain to both child classes.
    """
    file_type: ClassVar[str]
    glob_pattern: ClassVar[str]
    summarise_func: ClassVar
    _schema: ClassVar[dict]
    file_name: str | None
    file_extension: str | None
    projection: str | None
    supplied_tile_index_file: Path | None

    def bounding_box(self) -> Polygon:  # type: ignore
        pass

    def is_file_name_correct_format(self) -> bool:  # type: ignore
        pass

    def is_in_supplied_tile_index(self) -> bool:
        """
        Uses a spatial index of the supplied tile index to find the geometry of intersecting bounding boxes.
        It then uses the list of gemoetries to determine if the geometries of the file intersect with the geometry of the supplied tile index.
        Returns True if there is more than 0 intersecting geometries.
        Returns False if there are 0 intersecting geometries.
        """
        if self.supplied_tile_index_file is None:
            return False
        supplied_tile_index = self._get_spatial_index(self.supplied_tile_index_file)
        geoms = supplied_tile_index.geometries[supplied_tile_index.query(self.bounding_box())]
        for geom in geoms:
            if geom.intersection(self.bounding_box()).area > 0:
                return True
        return False

    def is_file_name_correct_tile(self) -> bool:
        """
        Uses the file polygon bounds to get a centroid which is used to get the official 1k tile, using index_tiles.py.
        Returns True if the file name mapsheet and tile number match the official 1k tile, False if either one doesn't match.
        """
        try:
            official_tile = official_tile_index.get_tile_from_point(self.bounding_box().centroid)
        except ValueError:
            logger.error(f"{self.file_name} is outside tile scheme")
            return False
        if official_tile is None or not self.file_name:
            return False
        return official_tile.sheet_code in self.file_name and official_tile.id in self.file_name

    def is_tiled_correctly(self) -> bool:
        """
        Uses the file polygon bounds to get a centroid which is used to get the official tile, using index_tiles.py.
        Returns True if file geometry is equal to the official tile, within a tolerance of 0.015cm.
        Returns False if the geometries don't match.
        """
        try:
            official_tile = official_tile_index.get_tile_from_point(self.bounding_box().centroid)
        except ValueError:
            logger.error(f"{self.file_name} is not tiled correctly - outside tile scheme")
            official_tile = None
        if official_tile is None:
            return False
        threshold = 0.015
        min_x, min_y, max_x, max_y = shapely.bounds(self.bounding_box())
        return all(
            [
                0 >= official_tile.min_x - min_x >= -threshold,  # not over 0, not lower than -0.015
                0 >= official_tile.min_y - min_y >= -threshold,  # not over 0, not lower than -0.015
                0 <= official_tile.max_x - max_x <= threshold,  # not under 0, not larger than 0.015
                0 <= official_tile.max_y - max_y <= threshold,  # not under 0, not larger than 0.015
            ]
        )

    def is_projection_correct_espg(self) -> bool:
        """
        Returns True if all three elements in the list are found in the wkt.
        Returns False if any one doesn't match the wkt.
        """
        if self.projection is None:
            return False
        return all(
            [
                "NZGD2000 / New Zealand Transverse Mercator 2000"
                or "NZGD2000_New_Zealand_Transverse_Mercator_2000" in self.projection,
                "New Zealand Geodetic Datum 2000" or "New_Zealand_Geodetic_Datum_2000" in self.projection,
                "2193" in self.projection,
            ]
        )

    def get_correct_tile(self) -> Dict:
        """
        Uses the file centroid to get the official 1k tile, using index_tiles.py.
        Returns official tile if within tile scheme.
        """
        try:
            official_tile = official_tile_index.get_tile_from_point(self.bounding_box().centroid)
        except ValueError:
            logger.error(f"{self.file_name} is outside tile scheme")
        
        return official_tile       

    @staticmethod
    def _get_spatial_index(vector_file: Path):
        """
        Receives path to the a file that fiona can open.
        Creates a STRtree spatial index of all features in the fiona openable file.
        Spatial indexes are stored in a global variable (dictionary).
        If the function is run multiple times, it will return the previously opened/created STRtree.
        Returns the spatial index.
        """
        global _strtrees
        if index := _strtrees.get(vector_file, None):
            return index
        with fiona.open(vector_file) as src:
            index = STRtree([shape(feat["geometry"]) for feat in src])
            _strtrees[vector_file] = index
        return index
