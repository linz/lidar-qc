import typer

from lidar_qc.cli.commands.build_vrt import build_vrt
from lidar_qc.cli.commands.check_dataset import check_dataset
from lidar_qc.cli.commands.density_rasters import density_raster
from lidar_qc.cli.commands.difference_raster import difference_raster
from lidar_qc.cli.commands.neighbour_raster import neighbour_raster
from lidar_qc.cli.commands.psid import psid
from lidar_qc.cli.commands.rename import rename

app = typer.Typer(add_completion=False, pretty_exceptions_show_locals=False)
app.command()(check_dataset)
app.command()(psid)
app.command()(build_vrt)
app.command()(density_raster)
app.command()(neighbour_raster)
app.command()(difference_raster)
app.command()(rename)

if __name__ == "__main__":
    app()
