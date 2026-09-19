#!/usr/bin/env python3
"""Combine a charge-renormalized core RTF with fragment PRES blocks."""

from pathlib import Path


def combine_rtf_files(core_rtf_path, patches_dir, output_rtf_path):
    core_rtf_path = Path(core_rtf_path)
    patches_dir = Path(patches_dir)
    output_rtf_path = Path(output_rtf_path)

    combined = []
    seen_core = False

    with core_rtf_path.open() as handle:
        for line in handle:
            if line.strip().upper() == "END":
                continue
            if not seen_core and line.lstrip().startswith("RESI"):
                combined.append(line)
                seen_core = True
                continue
            if seen_core and line.lstrip().startswith("RESI") and " LIG " in line:
                continue
            combined.append(line)

    combined.append("\n")

    for rtf_path in sorted(patches_dir.glob("*_pres.rtf")):
        lines = rtf_path.read_text().splitlines(keepends=True)
        start = 0
        while start < len(lines) and (
            not lines[start].strip()
            or lines[start].lstrip().startswith("*")
            or lines[start].strip() == "36 1"
        ):
            start += 1

        block = [line for line in lines[start:] if line.strip().upper() != "END"]
        while block and not block[-1].strip():
            block.pop()

        combined.append("\n")
        combined.extend(block)

    combined.append("\nEND\n")
    output_rtf_path.parent.mkdir(parents=True, exist_ok=True)
    output_rtf_path.write_text("".join(combined))
    print(f"Combined RTF written to {output_rtf_path}")
