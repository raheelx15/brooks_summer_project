#!/usr/bin/env python3
"""Identify inconsistent atom mappings across aligned MOL2 files.

For a set of protonation-state MOL2 files that have been inverse-mapped into a
common coordinate frame, atoms with the same name should map to the same
coordinates. This utility collects coordinates by atom name and reports names
whose coordinates differ across files.
"""

from collections import defaultdict
from pathlib import Path
import argparse


def read_atom_coordinates(mol2_path: Path) -> dict[str, tuple[float, float, float]]:
    """Return {atom_name: (x, y, z)} from the ATOM section of a MOL2 file."""
    coordinates = {}
    in_atom_section = False

    with mol2_path.open() as handle:
        for raw_line in handle:
            line = raw_line.strip()

            if line.startswith("@<TRIPOS>ATOM"):
                in_atom_section = True
                continue
            if line.startswith("@<TRIPOS>BOND"):
                break

            if not in_atom_section:
                continue

            fields = line.split()
            if len(fields) < 5:
                continue

            atom_name = fields[1]
            x, y, z = map(float, fields[2:5])
            coordinates[atom_name] = (x, y, z)

    return coordinates


def find_conflicting_atoms(
    mol2_dir: Path,
) -> dict[str, dict[str, tuple[float, float, float]]]:
    """Find atom names assigned to different coordinates across MOL2 files."""
    atom_coords_across_files = defaultdict(dict)

    for mol2_path in sorted(mol2_dir.glob("*.mol2")):
        for atom_name, coords in read_atom_coordinates(mol2_path).items():
            atom_coords_across_files[atom_name][mol2_path.name] = coords

    conflicting_atoms = {}
    for atom_name, file_coords in atom_coords_across_files.items():
        if len(set(file_coords.values())) > 1:
            conflicting_atoms[atom_name] = file_coords

    return conflicting_atoms


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Flag inconsistent atom mappings across aligned MOL2 files."
    )
    parser.add_argument(
        "mol2_dir",
        type=Path,
        help="Directory containing aligned MOL2 files",
    )
    args = parser.parse_args()

    conflicts = find_conflicting_atoms(args.mol2_dir)

    if not conflicts:
        print("No conflicting atom mappings found.")
        return

    print(f"Found {len(conflicts)} conflicting atom name(s):")
    for atom_name, file_coords in sorted(conflicts.items()):
        print(f"\n{atom_name}")
        for filename, coords in sorted(file_coords.items()):
            print(f"  {filename}: {coords}")


if __name__ == "__main__":
    main()
