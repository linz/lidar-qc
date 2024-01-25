from pathlib import Path

import numpy as np
import rasterio
from scipy import ndimage


def calculate_focal_range(subarr):
    """
    Calculation to perform on the kernel window array.
    Returns the range between pixel values in the kernel window by minussing the min from the max value.
    """
    return subarr.max() - subarr.min()


def create_raster_per_tile(file: Path, output_dir: Path) -> None:
    # src is the input raster file. It is being read by rasterio which returns a numpy.ndarray type
    """
    The input raster file is opened with rasterio and read to return a numpy.ndarray type.
    This array is analysed to find the range between pixels and their neighbours within a 3x3 kernel, using a filter window method.
    The filtered array is written to a tif output using rasterio.
    """
    src = rasterio.open(file)
    src_band1 = src.read(1)
    process_arr = ndimage.generic_filter(input=src_band1, function=calculate_focal_range, footprint=np.ones((3, 3)))
    with rasterio.open(
        f"{output_dir / file.name}",
        "w",
        driver="GTiff",
        width=src_band1.shape[1],
        height=src_band1.shape[0],
        count=1,
        crs=rasterio.CRS.from_epsg(2193),
        transform=src.transform,
        dtype=src_band1.dtype,
        nodata=-9999,
    ) as dst:
        dst.write(process_arr, 1)
