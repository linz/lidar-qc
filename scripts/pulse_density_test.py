"""
Known-answer test for the pulse density raster.

`make` writes LAZ tiles with exactly N pulses in every 1 m x 1 m square (default 8).
Each pulse has 1-4 returns, and its last return is classified ground, so in every square:
    pulse density  = N exactly  (first returns that are not withheld, synthetic or key points)
    ground density = N exactly  (one ground point per pulse)
Extra withheld and synthetic first returns are scattered through the tiles. They are not
real pulses, so the pulse raster must ignore them.

`check` reads the rasters density-raster produced and reports any cell that isn't N.

Usage (in the lidar-qc conda env):
    python scripts/pulse_density_test.py make --output test_data/pulse_8ppsm
    linz-lidar-qc density-raster --input test_data/pulse_8ppsm --filter pulse --filter ground
    python scripts/pulse_density_test.py check --input test_data/pulse_8ppsm
"""

import argparse
import json
from pathlib import Path

import numpy as np

# NZTM2000 coordinates on whole metres, so tile edges and 1 m squares line up.
DEFAULT_ORIGIN = (1_570_000, 5_180_000)


def make_tile(x0: int, y0: int, size: int, density: int, rng: np.random.Generator,
              keypoint_fraction: float) -> np.ndarray:
    cells_x, cells_y = np.meshgrid(np.arange(size), np.arange(size))
    cells_x = np.repeat(cells_x.ravel(), density)
    cells_y = np.repeat(cells_y.ravel(), density)
    n_pulses = cells_x.size

    # Random positions inside each 1 m square, stored to the millimetre. Keep every point at
    # least 1 mm inside its square: a point exactly on a cell edge could fairly be counted in
    # either neighbouring cell, which would make the expected answer ambiguous.
    px = x0 + cells_x + np.round(rng.uniform(0.001, 0.999, n_pulses), 3)
    py = y0 + cells_y + np.round(rng.uniform(0.001, 0.999, n_pulses), 3)
    n_returns = rng.integers(1, 5, n_pulses)
    ground_z = 100 + rng.normal(0, 0.05, n_pulses)

    # Expand pulses into returns. All returns of a pulse share its x/y.
    pulse_idx = np.repeat(np.arange(n_pulses), n_returns)
    return_number = np.concatenate([np.arange(1, n + 1) for n in n_returns])
    nr = n_returns[pulse_idx]
    is_last = return_number == nr

    dtype = [("X", "f8"), ("Y", "f8"), ("Z", "f8"), ("Intensity", "u2"),
             ("ReturnNumber", "u1"), ("NumberOfReturns", "u1"), ("Classification", "u1"),
             ("Withheld", "u1"), ("Synthetic", "u1"), ("KeyPoint", "u1"), ("Overlap", "u1"),
             ("GpsTime", "f8"), ("PointSourceId", "u2")]
    pts = np.zeros(pulse_idx.size, dtype=dtype)
    pts["X"] = px[pulse_idx]
    pts["Y"] = py[pulse_idx]
    pts["Z"] = ground_z[pulse_idx] + np.where(is_last, 0, (nr - return_number) * 3.0)
    pts["Intensity"] = rng.integers(50, 4000, pulse_idx.size)
    pts["ReturnNumber"] = return_number
    pts["NumberOfReturns"] = nr
    # Last return is ground; earlier returns are low, medium or high vegetation.
    pts["Classification"] = np.where(is_last, 2, 3 + np.minimum(nr - return_number - 1, 2))
    pts["GpsTime"] = pulse_idx * 1e-5
    pts["PointSourceId"] = 1

    if keypoint_fraction > 0:
        # Flag some single-return pulses as model key points. They are still real pulses.
        single = np.flatnonzero((nr == 1) & is_last)
        pick = rng.choice(single, int(len(single) * keypoint_fraction), replace=False)
        pts["KeyPoint"][pick] = 1

    # Decoys: first returns that are not real pulses and must not be counted.
    n_decoy = n_pulses // 20
    decoys = np.zeros(2 * n_decoy, dtype=dtype)
    decoys["X"] = x0 + np.round(rng.uniform(0.001, size - 0.001, 2 * n_decoy), 3)
    decoys["Y"] = y0 + np.round(rng.uniform(0.001, size - 0.001, 2 * n_decoy), 3)
    decoys["Z"] = 100
    decoys["ReturnNumber"] = 1
    decoys["NumberOfReturns"] = 1
    decoys["Classification"] = 1
    decoys["Withheld"][:n_decoy] = 1
    decoys["Synthetic"][n_decoy:] = 1
    decoys["PointSourceId"] = 1
    return np.concatenate([pts, decoys])


def make(args: argparse.Namespace) -> None:
    import pdal

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    for tx in range(args.tiles):
        for ty in range(args.tiles):
            x0 = args.origin_x + tx * args.tile_size
            y0 = args.origin_y + ty * args.tile_size
            pts = make_tile(x0, y0, args.tile_size, args.density, rng, args.keypoints)
            name = out / f"pulse_test_{x0}_{y0}.laz"
            pdal.Pipeline(json.dumps([{
                "type": "writers.las", "filename": str(name), "compression": True,
                "minor_version": 4, "dataformat_id": 6, "a_srs": "EPSG:2193",
                "scale_x": 0.001, "scale_y": 0.001, "scale_z": 0.001,
                "offset_x": "auto", "offset_y": "auto", "offset_z": "auto",
            }]), arrays=[pts]).execute()
            print(f"wrote {name.name}: {len(pts):,} points, "
                  f"{args.tile_size * args.tile_size * args.density:,} pulses")
    print(f"\nEvery 1 m square has exactly {args.density} pulses and {args.density} ground points.")
    if args.keypoints:
        print(f"{args.keypoints:.0%} of single-return pulses are flagged as key points.")


def summarise(folder: Path, expected: int) -> bool:
    import rasterio

    tifs = sorted(folder.glob("*.tif"))
    if not tifs:
        print(f"{folder.name}: no rasters found")
        return False
    ok = True
    print(f"\n{folder.name} (expected {expected} in every cell)")
    for tif in tifs:
        with rasterio.open(tif) as r:
            a = r.read(1)
            t = r.transform
        valid = a[a != -9999]
        interior = a[1:-1, 1:-1]
        bad = int((interior != expected).sum())
        aligned = abs(t.c - round(t.c)) < 1e-6 and abs(t.f - round(t.f)) < 1e-6
        values, counts = np.unique(valid, return_counts=True)
        spread = ", ".join(f"{v}: {c}" for v, c in zip(values, counts))
        print(f"  {tif.name}: {a.shape[1]} x {a.shape[0]} cells, grid on whole metres: {aligned}")
        print(f"    interior cells not {expected}: {bad}/{interior.size}; mean {valid.mean():.3f}")
        print(f"    values (value: cells): {spread}")
        ok &= bad == 0 and aligned
    return ok


def check(args: argparse.Namespace) -> None:
    root = Path(args.input)
    results = [summarise(root / f"{name}_raster", args.density) for name in ("pulse", "ground")]
    print("\nPASS" if all(results) else "\nFAIL: see the cells above that are not the expected value")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make", help="write the test tiles")
    m.add_argument("--output", required=True)
    m.add_argument("--density", type=int, default=8, help="pulses per square metre (default 8)")
    m.add_argument("--tile-size", type=int, default=100, help="tile edge in metres (default 100)")
    m.add_argument("--tiles", type=int, default=2, help="tiles per side, so 2 makes a 2 x 2 block")
    m.add_argument("--origin-x", type=int, default=DEFAULT_ORIGIN[0])
    m.add_argument("--origin-y", type=int, default=DEFAULT_ORIGIN[1])
    m.add_argument("--keypoints", type=float, default=0.0,
                   help="fraction of single-return pulses to flag as key points (default 0)")
    m.add_argument("--seed", type=int, default=8)
    m.set_defaults(func=make)
    c = sub.add_parser("check", help="check the rasters density-raster made")
    c.add_argument("--input", required=True, help="the folder of test tiles")
    c.add_argument("--density", type=int, default=8)
    c.set_defaults(func=check)
    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
