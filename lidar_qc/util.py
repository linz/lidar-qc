def is_point_cloud_dir(name: str) -> bool:
    """
    Receives folder path and returns True if point, laz, or las is in the folder name.
    """
    return "point" in name.lower() or "laz" in name.lower() or "las" in name.lower()


def is_raster_dir(name: str) -> bool:
    """
    Receives folder path and returns True if dem or dsm is in the folder name.
    """
    return "dem" in name.lower() or "dsm" in name.lower()
