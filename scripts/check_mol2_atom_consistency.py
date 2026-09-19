#!/usr/bin/env python3
"""Flag inconsistent atom mappings across aligned MOL2 files.

This utility was written while extending the ligand-parameterization workflow
to detect atom-name mappings that differed across protonation-state MOL2 files.
"""

from collections import defaultdict
from pathlib import Path
import argparse


def read_atom_coordinates(mol2_path: Path) -> dict[str, tuple[float, float, float]]:
    """Return atom-name -> (x, y, z) coordinates from a MOL2 ATOM section."""
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
            coordinates[atom_name] = tuple(map(float, fields[2:5]))

    return coordinates


def find_conflicting_atoms(mol2_dir: Path):
    """Return atoms whose coordinates differ between state-specific MOL2 files."""
    atom_coords_across_files = defaultdict(dict)

    for mol2_path in sorted(mol2_dir.glob("*.mol2")):
        for atom_name, coords in read_atom_coordinates(mol2_path).items():
            atom_coords_across_files[atom_name][mol2_path.name] = coords

    return {
        atom_name: file_coords
        for atom_name, file_coords in atom_coords_across_files.items()
        if len(set(file_coords.values())) > 1
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Flag inconsistent atom mappings across aligned MOL2 files."
    )
    parser.add_argument("mol2_dir", type=Path)
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
