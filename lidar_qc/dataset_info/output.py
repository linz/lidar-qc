import sqlite3
from pathlib import Path
from typing import Dict, List, Tuple, Union

import fiona
import fiona.collection
from fiona.crs import from_epsg

from lidar_qc.dataset_info.point_cloud_file_info import PointCloudFileInfo
from lidar_qc.dataset_info.raster_file_info import RasterFileInfo
from lidar_qc.log import get_logger
from lidar_qc.parallel import ParallelErrorInfo
from lidar_qc.util import is_point_cloud_dir, is_raster_dir

logger = get_logger()

ERROR_SCHEMA = {
    "geometry": "GeometryCollection",
    "properties": {"file": "str", "errors": "str"},
}


def save_to_gpkg(
    output_gpkg: Path,
    dataset_infos: Dict[str, Union[List[RasterFileInfo], List[PointCloudFileInfo]]],
    dataset_infos_errors: Dict[str, List[ParallelErrorInfo]],
    product_summaries: Dict[str, List[Tuple[str, str, str]]],
) -> None:
    """
    Adds features to product tile index's in empty geopackage using Fiona, for each raw data directory.
    Uses sqlite to create a summary table in the geopakcage and add the product summaries.
    It also adds symbology to the product tile index's using splite and QGIS style files.
    Any errors during splite process is captured as an exception and logged to terminal.

    Args:
        dataset_infos: dictionary where the key is raw data directory and value is a list of either point cloud or raster file info class instances.
        output_gpkg: file path to geopackage, specified in command line.
        product_summaries: dictionary where the key is the product name and the value is a list of tuples[check, standard, value].

    No returns.
    """
    for raw_data_dir, file_infos in dataset_infos.items():
        file_info_cls = file_infos[0].__class__
        features = [file_info.feature() for file_info in file_infos]
        features = [feat for feat in features if feat is not None]
        with fiona.open(
            output_gpkg, "w", driver="GPKG", layer=raw_data_dir, schema=file_info_cls._schema, crs=from_epsg(2193)
        ) as output:
            logger.info(f"Writing {raw_data_dir} to geopackage")
            try:
                output.writerecords(features)
            except Exception as err:
                logger.error(f"Error encountered when writing data from {raw_data_dir} to geopackage: {err}")

    for raw_data_dir, file_infos_errors in dataset_infos_errors.items():
        table_name = f"{raw_data_dir}_errors"
        features = [
            {
                "geometry": {"type": "GeometryCollection", "geometries": []},
                "properties": {"file": str(file_infos_error.item), "errors": str(file_infos_error.error)},
            }
            for file_infos_error in file_infos_errors
        ]
        with fiona.open(output_gpkg, "w", driver="GPKG", layer=table_name, schema=ERROR_SCHEMA, crs=from_epsg(2193)) as output:
            logger.info(f"Writing {table_name} to geopackage")
            try:
                output.writerecords(features)
            except Exception as err:
                logger.error(f"Error encountered when writing errors from {raw_data_dir} to geopackage: {err}")

    summary_values = []
    layer_style_values = []
    classification_consistency_style = None
    raster_style = None
    for product_name, summary in product_summaries.items():
        if summary:
            for check, standard, value in summary:
                summary_values.append((product_name, check, standard, value))
            if is_point_cloud_dir(product_name):
                if classification_consistency_style is None:
                    style_file = Path(__file__).parents[1] / "layer_styles/point_cloud_style.qml"
                    classification_consistency_style = style_file.read_text()
                layer_style_values.append((product_name, classification_consistency_style))
            if is_raster_dir(product_name):
                if raster_style is None:
                    style_file = Path(__file__).parents[1] / "layer_styles/raster_style.qml"
                    raster_style = style_file.read_text()
                layer_style_values.append((product_name, raster_style))

    connection = sqlite3.connect(output_gpkg)
    cursor = connection.cursor()
    cursor.execute("BEGIN TRANSACTION")
    try:
        logger.info("Writing summary table and symbology to geopackage")
        # cursor.execute("PRAGMA application_id = 0x47504b47;")
        # cursor.execute("PRAGMA user_version = 0x000027D8;")
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS summary (
            product TEXT NOT NULL,
            "check" TEXT NOT NULL,
            standard TEXT,
            "value" TEXT,
            PRIMARY KEY (product, "check")
        );
        """
        )
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS layer_styles (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            f_table_catalog TEXT(256),
            f_table_schema TEXT(256),
            f_table_name TEXT(256),
            f_geometry_column TEXT(256),
            styleName TEXT(30),
            styleQML TEXT,
            styleSLD TEXT,
            useAsDefault BOOLEAN,
            description TEXT,
            owner TEXT(30),
            ui TEXT(30),
            update_time DATETIME DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
        );
        """
        )
        cursor.executemany(
            """
        INSERT OR REPLACE INTO layer_styles (
            f_table_catalog,
            f_table_schema,
            f_table_name,
            f_geometry_column,
            styleName,
            styleQML,
            styleSLD,
            useAsDefault,
            description,
            owner
        )
        VALUES ('', '', (?), 'geom', 'Style', (?), '', true, '', '');
        """,
            layer_style_values,
        )
        cursor.executemany(
            """
        INSERT OR REPLACE INTO summary (product, "check", standard, "value")
        VALUES((?), (?), (?), (?));
        """,
            summary_values,
        )
        extra_table_details = [
            ("summary", "attributes", "summary", "", 0),
            ("layer_styles", "attributes", "layer_styles", "", 0),
        ]
        # for raw_data_dir, file_infos_errors in dataset_infos_errors.items():
        #     if file_infos_errors:
        #         table_name = f"{raw_data_dir}_errors"
        #         logger.info(f"Writing {table_name} to geopackage")
        #         extra_table_details.append((table_name, "attributes", table_name, "", 0))
        #         cursor.execute(
        #             f"""
        #         CREATE TABLE IF NOT EXISTS "{table_name}" (
        #             file TEXT PRIMARY KEY NOT NULL,
        #             errors TEXT NOT NULL
        #         );
        #         """
        #         )
        #         cursor.executemany(
        #             f"""
        #         INSERT OR REPLACE INTO "{table_name}" (file, errors)
        #         VALUES ((?), (?));
        #         """,
        #             [(Path(error.item).name, str(error.error)) for error in file_infos_errors],
        #         )
        # cursor.execute(
        #     """
        # CREATE TABLE IF NOT EXISTS gpkg_spatial_ref_sys (
        #     srs_name TEXT NOT NULL,
        #     srs_id INTEGER NOT NULL PRIMARY KEY,
        #     organization TEXT NOT NULL,
        #     organization_coordsys_id INTEGER NOT NULL,
        #     definition  TEXT NOT NULL,
        #     description TEXT
        # );
        # """
        # )
        # for values in [
        #     ("Undefined Cartesian SRS", -1, "NONE", -1, "undefined", "undefined Cartesian coordinate reference system"),
        #     ("Undefined geographic SRS", 0, "NONE", 0, "undefined", "undefined geographic coordinate reference system"),
        #     (
        #         "WGS 84 geodetic",
        #         4326,
        #         "EPSG",
        #         4326,
        #         'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AXIS["Latitude",NORTH],AXIS["Longitude",EAST],AUTHORITY["EPSG","4326"]]',
        #         "longitude/latitude coordinates in decimal degrees on the WGS 84 spheroid",
        #     ),
        # ]:
        #     cursor.execute(
        #         f"""
        #     INSERT INTO gpkg_spatial_ref_sys (srs_name, srs_id, organization, organization_coordsys_id, definition, description)
        #     VALUES ((?), (?), (?), (?), (?), (?))
        #     EXCEPT
        #     SELECT * FROM gpkg_spatial_ref_sys WHERE srs_id = {values[1]};
        #     """,
        #         values,
        #     )
        # cursor.execute(
        #     """
        # CREATE TABLE IF NOT EXISTS gpkg_contents (
        #     table_name TEXT NOT NULL PRIMARY KEY,
        #     data_type TEXT NOT NULL,
        #     identifier TEXT UNIQUE,
        #     description TEXT DEFAULT '',
        #     last_change DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
        #     min_x DOUBLE,
        #     min_y DOUBLE,
        #     max_x DOUBLE,
        #     max_y DOUBLE,
        #     srs_id INTEGER,
        #     CONSTRAINT fk_gc_r_srs_id FOREIGN KEY (srs_id) REFERENCES gpkg_spatial_ref_sys(srs_id)
        # );
        # """
        # )
        # # TODO work out how to write an empty feature/tile layer to geopackage. Else, save to text file lol.
        cursor.executemany(
            """
        INSERT OR REPLACE INTO gpkg_contents (table_name, data_type, identifier, description, srs_id)
        VALUES ((?), (?), (?), (?), (?));
        """,
            extra_table_details,
        )
        cursor.execute("COMMIT;")
    except Exception as error:
        logger.error(f"{error}: Error updating database, rolling back")
        cursor.execute("ROLLBACK;")
