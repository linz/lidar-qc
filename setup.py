from setuptools import find_packages, setup

setup(
    name="linz-lidar-qc",
    version="0.1",
    description="Tools for the performing QC of lidar datasets.",
    install_requires=[],
    setup_requires=[],
    packages=find_packages(exclude=["examples", "tests"]),
    entry_points="""
        [console_scripts]
        linz-lidar-qc=lidar_qc.cli.main:app
    """,
)
