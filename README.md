# Constant-pH MD Ligand Parameterization

Research code and preprocessing outputs from my 2025 work in the **Charles L. Brooks III Lab at the University of Michigan**, focused on preparing titratable small-molecule ligands for constant-pH molecular dynamics (CpHMD) with multisite λ-dynamics.

## Project overview

Ligand protonation can change with environment and strongly influence conformation, protein–ligand interactions, and binding thermodynamics. This project focused on constructing and validating multistate ligand representations for CHARMM-based CpHMD and applying the workflow to riboflavin.

The curated workflow is in [`notebooks/riboflavin_parameterization_workflow.ipynb`](notebooks/riboflavin_parameterization_workflow.ipynb).

## My contributions

My project-specific work included:

- automating ligand preprocessing and CGenFF parameter-generation steps;
- aligning protonation states and preparing consistent MOL2/RTF/PRM inputs;
- building validation checks for atom-name and atom-mapping consistency across states;
- selecting reference states using ligand charge and CGenFF penalty information;
- integrating charge-renormalized core/patch files into CHARMM-compatible topology and parameter files;
- generating CHARMM build inputs and debugging parameterization/compatibility issues; and
- running and analyzing the resulting CpHMD/ALF workflow on HPC resources.

The underlying **multisite λ-dynamics, Adaptive Landscape Flattening (ALF), MCS, and charge-renormalization methodology/helper code** was developed by the Brooks Lab and collaborators. Lab-provided helper implementations used in this project are separated under [`scripts/brooks_lab/`](scripts/brooks_lab/) to make provenance explicit.

## Featured code sample

[`scripts/check_mol2_atom_consistency.py`](scripts/check_mol2_atom_consistency.py) is a validation utility I wrote after encountering difficult atom-mapping inconsistencies during ligand parameterization. It compares atom coordinates across aligned, state-specific MOL2 files and flags atom names whose mappings differ between states.

This automated a debugging step I had initially performed manually and helped catch subtle inconsistencies before they propagated into the larger simulation workflow.

## Repository structure

```text
.
├── notebooks/
│   └── riboflavin_parameterization_workflow.ipynb
├── scripts/
│   ├── check_mol2_atom_consistency.py
│   ├── combine_rtf_files.py
│   └── brooks_lab/
│       ├── msld_mcs.py
│       └── msld_crn.py
├── preprocessing/
│   ├── input_data/
│   ├── cgenff_output/
│   ├── structure_conversion/
│   ├── alignment/
│   ├── mcs/
│   ├── charge_renormalization/
│   └── charmm_setup/
└── reference/
    ├── phenol/
    └── pdb/
```

## Main tools

Python, RDKit, Open Babel, pandas/NumPy, CHARMM/pyCHARMM, CGenFF, multisite λ-dynamics, Adaptive Landscape Flattening, shell/HPC workflows.

## Research output

This work contributed to the peer-reviewed Biophysical Society abstract:

**Cherepanov, Sarwar, Brooks. “Making ligands titratable: Extending CpHMD with drug binding.”**
*Biophysical Journal* (2026).
**DOI:** https://doi.org/10.1016/j.bpj.2025.11.2197

A full manuscript describing the methodology and results is in preparation.

## Repository note

This repository reflects an academic research workflow rather than a standalone software package. Some steps depend on laboratory/HPC software that is not distributed here. Intermediate files are retained to document the actual preprocessing sequence used during the project.
