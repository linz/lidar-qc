import subprocess
from pathlib import Path


def decompress_file(file: Path, output_dir: Path) -> None:
    output_las: Path = output_dir / f"{file.stem}.las"
    args = ["C:/LAStools/bin/laszip.exe", "-i", str(file), "-o", str(output_las)]
    result = subprocess.run(args=args, capture_output=True, shell=True, encoding="utf-8", check=True)
    if result.stderr and not result.stderr.startswith('Please note that LAStools is not "free"'):
        raise RuntimeError(f"Subprocess Error: {result.stderr}")
