from pathlib import Path

import numpy as np
import rasterio
from scipy import ndimage


def calculate_focal_range(subarr):
    """
    Calculation to perform on the kernel window array.
    Returns the range between pixel values in the kernel window by minusing the min from the max value.
    """
    return subarr.max() - subarr.min()


def create_neighbour_raster(file: Path, output_dir: Path) -> None:
    """
    The input raster file is opened with rasterio and read to a numpy.ndarray type.
    This array is run through a filter which uses a moving 3x3 kernel window to find the range
    between pixels and their neighbours, across the array.
    The filtered array is written to a tif output using rasterio.
    """
    src = rasterio.open(file)
    src_arr = src.read(1)
    range_arr = ndimage.generic_filter(input=src_arr, function=calculate_focal_range, footprint=np.ones((3, 3)))
    with rasterio.open(
        f"{output_dir / file.name}",
        "w",
        driver="GTiff",
        width=src_arr.shape[1],
        height=src_arr.shape[0],
        count=1,
        crs=rasterio.CRS.from_epsg(2193),
        transform=src.transform,
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
