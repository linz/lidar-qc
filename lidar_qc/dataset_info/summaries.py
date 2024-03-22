from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING, Collection, List, Tuple

import fiona

if TYPE_CHECKING:
    from lidar_qc.dataset_info.point_cloud_file_info import PointCloudFileInfo
    from lidar_qc.dataset_info.raster_file_info import RasterFileInfo

# def summarise_product():
#     check_data = defaultdict(list)
#     for file_info in file_infos:
#         for func in [summarise_file_source_id]:
#             key, value = func(file_info)
#             check_data[key].append(value)


def summarise_supplied_tile_index(supplied_tile_index: Path | None) -> List[Tuple[str, str, str]] | None:
    """
    Receives a path to the supplied tile index input at command line or None.
    Opens the tile index with Fiona to get the feature count.
    Returns the feature count in a tuple, structured for the summary table.
    """
    if supplied_tile_index is None:
        return None
    with fiona.open(supplied_tile_index) as src:
        feature_count = len(src)
    return [("Feature count", "", str(feature_count))]


def summarise_raster_product(file_infos: List["RasterFileInfo"]) -> List[Tuple[str, str, str]]:
    """
    List of raster file info instances are looped through to test a series of bool statements, based on linz-spec.
    The result of these bool tests are appended to a dictionary of lists, which are used to summarised file metadata information at product scale.
    Returns list of tuples where each string in the tuple relates to a field in the summarise table in the output geopackage.
    """
    check_data = defaultdict(list)
    for file_info in file_infos:
        check_data["nodata"].append(file_info.nodata == -9999)
        check_data["width"].append(file_info.file_size.x == 480)
        check_data["height"].append(file_info.file_size.y == 720)
        check_data["pixel_x"].append(file_info.pixel_size.x == 1)
        check_data["pixel_y"].append(file_info.pixel_size.y == -1)
        check_data["origin_x"].append(file_info.origin.x % 1 == 0)
        check_data["origin_y"].append(file_info.origin.y % 1 == 0)
        check_data["file_type"].append(file_info.data_type == "Float32")
        check_data["max_pixel_value"].append(file_info.max_pixel_value)
        check_data["min_pixel_value"].append(file_info.min_pixel_value)
        check_data["name_format"].append(file_info.is_file_name_correct_format())
        check_data["name_tile"].append(file_info.is_file_name_correct_tile())
        check_data["coordinates"].append(file_info.is_tiled_correctly())
        check_data["supplied_index"].append(file_info.is_in_supplied_tile_index())
        check_data["projection"].append(file_info.is_projection_correct_espg())

    def all_true(key: str, value_if_true: str = "Yes", value_if_false: str = "No") -> str:
        return value_if_true if all(check_data[key]) else value_if_false

    return [
        ("Is the nodata value correct?", "-9999", all_true("nodata")),
        ("Is width correct?", "480", all_true("width")),
        ("Is height correct?", "720", all_true("height")),
        ("Is pixel x correct?", "1", all_true("pixel_x")),
        ("Is pixel y correct?", "-1", all_true("pixel_y")),
        ("Is origin x whole metre?", "no decimal values", all_true("origin_x")),
        ("Is origin y whole metre?", "no decimal values", all_true("origin_y")),
        ("Is file type correct?", "Float32", all_true("file_type")),
        ("Minimum pixel value for dataset", "", str(min(check_data["min_pixel_value"]))),
        ("Maximum pixel value for dataset", "", str(max(check_data["max_pixel_value"]))),
        ("Is the name format correct?", "product_sheet_date_scale_tile", all_true("name_format")),
        ("Does the tile name match LINZ official tiles?", "sheet and tile number", all_true("name_tile")),
        ("Does the coordinates match LINZ official tiles?", "", all_true("coordinates")),
        ("Are all tiles within the supplied tile index?", "", all_true("supplied_index")),
        (
            "Does WKT have correct projection and horizontal datum flags?",
            "NZGD 2000 / New Zealand Transverse Mercator 2000, New Zealand Geodetic Datum 2000, 2193",
            all_true("projection"),
        ),
        ("Feature count", "", str(len(file_infos))),
    ]


def filter_none(items: Collection):
    return filter(lambda v: v is not None, items)


def filter_zero(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return a / b


def summarise_point_cloud_product(file_infos: List["PointCloudFileInfo"]) -> List[Tuple[str, str, str]]:
    """
    List of point cloud file info instances are looped through to test a series of bool statements, based on linz-spec.
    The result of these bool tests are appended to a dictionary of lists, which are used to summarised file metadata information at product scale.
    Returns list of tuples where each string in the tuple relates to a field in the summarise table in the output geopackage.
    """
    check_data = defaultdict(list)
    for file_info in file_infos:
        check_data["file_source_id"].append(file_info.header_file_source_id == 0)
        check_data["global_encoding"].append(file_info.header_global_encoding == 17)
        check_data["las_version"].append(file_info.version() == "1.4")
        check_data["data_format"].append(file_info.is_point_data_format_correct())
        check_data["min_z"].append(file_info.header_coordinates_min.z)
        check_data["max_z"].append(file_info.header_coordinates_max.z)
        check_data["min_intensity"].append(file_info.point_data_intensity.min)
        check_data["max_intensity"].append(file_info.point_data_intensity.max)
        check_data["min_return"].append(file_info.point_data_return_number.min)
        check_data["max_return"].append(file_info.point_data_return_number.max)
        check_data["min_scan_angle"].append(file_info.point_data_scan_angle_rank.min)
        check_data["max_scan_angle"].append(file_info.point_data_scan_angle_rank.max)
        check_data["min_psid"].append(file_info.point_data_point_source_id.min)
        check_data["max_psid"].append(file_info.point_data_point_source_id.max)
        check_data["min_gps"].append(file_info.point_data_gps_time.min)
        check_data["max_gps"].append(file_info.point_data_gps_time.max)
        check_data["scale_factor"].append(file_info.is_scale_factor_correct())
        check_data["name_format"].append(file_info.is_file_name_correct_format())
        check_data["name_tile"].append(file_info.is_file_name_correct_tile())
        check_data["supplied_index"].append(file_info.is_in_supplied_tile_index())
        check_data["coordinates"].append(file_info.is_tiled_correctly())
        check_data["projection"].append(file_info.is_projection_correct_espg())
        check_data["vert_datum"].append(file_info.is_vertical_datum_correct())
        check_data["classifications"].append(set(file_info.classifications.keys()))
        check_data["overlap"].append(bool(file_info.overlap_flag_classifications))
        check_data["withheld"].append(bool(file_info.withheld_flag_classifications))
        check_data["overlap_total_points"].append(file_info.overlap_total_points)
        check_data["total_points"].append(file_info.header_extended_number_of_points)
        if low_noise := file_info.classifications.get(7):
            check_data["low_noise"].append(low_noise.count)
        if high_noise := file_info.classifications.get(18):
            check_data["high_noise"].append(high_noise.count)
        check_data["pulse_density"].append(file_info.get_pulse_density_first_return())
        check_data["point_density"].append(file_info.get_point_density_per_tile())
        if not_classed := file_info.classifications.get(0):
            check_data["zero_class"].append(not_classed.id == 0)

    def all_true(key: str, value_if_true: str = "Yes", value_if_false: str = "No") -> str:
        return value_if_true if all(check_data[key]) else value_if_false

    def any_true(key: str, value_if_true: str = "Yes", value_if_false: str = "No") -> str:
        return value_if_true if any(check_data[key]) else value_if_false

    def dataset_classifications(key: str, dataset_classes: set = set()) -> str:
        for tile_class in check_data[key]:
            dataset_classes.update(tile_class)
        return str(dataset_classes)

    return [
        ("Is file source ID correct?", "0", all_true("file_source_id")),
        ("Is global encoding correct?", "17", all_true("global_encoding")),
        ("Is LAS file version correct?", "LAS 1.4", all_true("las_version")),
        ("Is point data format correct?", "6, 7, 8, 9, or 10", all_true("data_format")),
        ("Is scale factor correct?", "[0.001,0.001,0.001], [0.01,0.01,0.01], or [0.01,0.01,0.001]", all_true("scale_factor")),
        ("What is the Z value range?", "", f"{min(check_data['min_z'])} - {max(check_data['max_z'])}"),
        ("What is the intensity range?", "", f"{min(check_data['min_intensity'])} - {max(check_data['max_intensity'])}"),
        ("What is the return number range?", "", f"{min(check_data['min_return'])} - {max(check_data['max_return'])}"),
        ("What is the scan angle range?", "", f"{min(check_data['min_scan_angle'])} - {max(check_data['max_scan_angle'])}"),
        ("What is the point source ID range?", "", f"{min(check_data['min_psid'])} - {max(check_data['max_psid'])}"),
        ("What is the gps time range?", "", f"{min(check_data['min_gps'])} - {max(check_data['max_gps'])}"),
        ("Dataset classification IDs", "1,2,3,4,5,6,7,9,18", dataset_classifications("classifications")),
        ("Are there any tiles with class 0?", "Class 0 points must be withheld", any_true("zero_class")),
        (
            "Pulse density for dataset by first returns",
            "4 or 8",
            f"{filter_zero(sum(filter_none(check_data['pulse_density'])), len(list(filter_none(check_data['pulse_density']))))}",
        ),
        (
            "Point density for dataset",
            "",
            f"{filter_zero(sum(filter_none(check_data['point_density'])), len(list(filter_none(check_data['point_density']))))}",
        ),
        ("Are there overlap points?", "", any_true("overlap")),
        ("Are there withheld points?", "", any_true("withheld")),
        ("Is the name format correct?", "product_sheet_date_scale_tile", all_true("name_format")),
        ("Does the tile name match LINZ official tiles?", "sheet and tile number", all_true("name_tile")),
        ("Are all tiles within the supplied tile index?", "", all_true("supplied_index")),
        ("Does the coordinates match LINZ official tiles?", "", all_true("coordinates")),
        (
            "Does WKT have correct projection and horizontal datum flags?",
            "NZGD 2000 / New Zealand Transverse Mercator 2000, New Zealand Geodetic Datum 2000, 2193",
            all_true("projection"),
        ),
        (
            "Does WKT have correct vertical datum flags?",
            "NZVD2016, New Zealand Vertical Datum 2016",
            all_true("vert_datum"),
        ),
        (
            "Percent of total overlap points in dataset",
            "",
            f"{filter_zero(sum(filter_none(check_data['overlap_total_points'])), sum(filter_none(check_data['total_points']))) * 100}",
        ),
        (
            "Percent of noise points in dataset",
            "",
            f"{filter_zero((sum(check_data['low_noise']) + sum(check_data['high_noise'])), sum(filter_none(check_data['total_points']))) * 100}",
        ),
        ("Feature count", "", str(len(file_infos))),
    ]
