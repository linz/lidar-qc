from pathlib import Path

import numpy as np
import rasterio
from scipy.ndimage import maximum_filter, minimum_filter


def calculate_focal_range(subarr):
    """
    Calculation to perform on the kernel window array.
    Returns the range between pixel values in the kernel window by minusing the min from the max value.
    """
    return subarr.max() - subarr.min()


def create_neighbour_raster(file: Path, output_dir: Path) -> None:
    with rasterio.open(file) as src:
        src_arr = src.read(1).astype(np.float32)
        transform = src.transform

    footprint = np.ones((3, 3))
    range_arr = maximum_filter(src_arr, footprint=footprint) - minimum_filter(
        src_arr, footprint=footprint
    )

    with rasterio.open(
        f"{output_dir / file.name}",
        "w",
        driver="GTiff",
        width=src_arr.shape[1],
        height=src_arr.shape[0],
        count=1,
        compress="lzw",
        crs=rasterio.CRS.from_epsg(2193),
        transform=transform,
        dtype=src_arr.dtype,
        nodata=-9999,
    ) as dst:
        dst.write(range_arr, 1)


def create_difference_raster(files: tuple[Path, Path], output_dir: Path) -> None:
    """
    The input tuple contains the path for the DEM and DSM file.
    Both raster files are opened with rasterio and read to a numpy.ndarray type.
    The DEM array is minused from the DSM array to find the difference between rasters.
    The difference array is written to a tif output using rasterio.
    """
    dem_src = rasterio.open(files[0])
    dem_arr = dem_src.read(1)
    dsm_arr = (rasterio.open(files[1])).read(1)
    diff_arr = dsm_arr - dem_arr
    with rasterio.open(
        f"{output_dir / files[0].name[4:]}",
        "w",
        driver="GTiff",
        width=dem_arr.shape[1],
        height=dem_arr.shape[0],
        count=1,
        crs=rasterio.CRS.from_epsg(2193),
        transform=dem_src.transform,
        dtype=dem_arr.dtype,
        nodata=-9999,
    ) as dst:
        dst.write(diff_arr, 1)
