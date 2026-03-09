import shutil
from pathlib import Path


KNOWN_EXECUTABLES = ["lasinfo", "lasinfo64", "laszip", "laszip64", "lasgrid", "lasgrid64"]


def find_lastools_exe(name: str) -> Path:
    """
    Locate a LAStools executable by name.

    Search order:
      1. LASTOOLS_BIN environment variable (e.g. LASTOOLS_BIN=C:/LAStools/bin)
      2. System PATH (e.g. if LAStools/bin is added to PATH)

    Raises FileNotFoundError with a clear message if the executable cannot be found.

    Example:
        laszip = find_lastools_exe("laszip")
        subprocess.run([str(laszip), "-i", str(file), ...])
    """
    import os

    # 1. Check LASTOOLS_BIN environment variable first
    env_bin = os.environ.get("LASTOOLS_BIN")
    if env_bin:
        for candidate in [f"{name}64.exe", f"{name}.exe", name]:
            exe = Path(env_bin) / candidate
            if exe.is_file():
                return exe
        raise FileNotFoundError(
            f"LASTOOLS_BIN is set to '{env_bin}' but '{name}' was not found there. "
            f"Check the path is correct and LAStools is installed."
        )

    # 2. Fall back to PATH
    exe = shutil.which(name) or shutil.which(f"{name}64")
    if exe:
        return Path(exe)

    raise FileNotFoundError(
        f"Could not find '{name}' on PATH or via LASTOOLS_BIN. "
        f"Ensure LAStools is installed and either:\n"
        f"  - Add LAStools to your PATH (e.g. C:\\LAStools\\bin), or\n"
        f"  - Set the LASTOOLS_BIN environment variable to your LAStools bin directory."
    )