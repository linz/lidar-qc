import typer

from lidar_qc.cli.commands.build_neighbours import build_neighbours
from lidar_qc.cli.commands.build_vrt import build_vrt
from lidar_qc.cli.commands.check_dataset import check_dataset
from lidar_qc.cli.commands.density_rasters import density_raster
from lidar_qc.cli.commands.psid import psid

app = typer.Typer(add_completion=False, pretty_exceptions_show_locals=False)
app.command()(check_dataset)
app.command()(psid)
app.command()(build_vrt)
app.command()(density_raster)
app.command()(build_neighbours)

if __name__ == "__main__":
    app()
