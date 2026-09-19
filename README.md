 Ligand Parameterization for Constant-pH Molecular Dynamics

Research code and intermediate files from my 2025 work in the Charles L. Brooks III Lab at the University of Michigan, focused on preparing titratable small-molecule ligands for constant-pH molecular dynamics (CpHMD) with multisite λ-dynamics.

Project overview

Ligand protonation can change with environment and can strongly affect molecular interactions and binding thermodynamics. This project focused on constructing and validating multistate ligand representations that could be used in CHARMM-based CpHMD workflows.

This repository documents the parameterization workflow I developed and adapted for riboflavin, including molecular-state preprocessing, CGenFF parameter generation, structural alignment, maximum-common-substructure analysis, charge renormalization, CHARMM topology/parameter assembly, and validation of atom mappings across protonation states.

My contributions

My project-specific work included:

Automating ligand preprocessing and CGenFF parameter-generation steps

Aligning protonation states and preparing consistent MOL2/RTF/PRM inputs

Building validation checks for atom-name and atom-mapping consistency across states

Selecting reference states using ligand charge and CGenFF penalty information

Integrating charge-renormalized core/patch files into CHARMM-compatible topology and parameter files

Generating CHARMM build inputs and debugging parameterization/compatibility issues

Running and analyzing the resulting constant-pH molecular-dynamics workflow on HPC resources

The underlying multisite λ-dynamics, Adaptive Landscape Flattening (ALF), MCS, and charge-renormalization methodology/helper code was developed by the Brooks Lab and collaborators. This repository is intended to highlight my project-specific preprocessing, validation, integration, and analysis work rather than claim authorship of the underlying simulation framework.

Featured code sample

scripts/check_mol2_atom_consistency.py is a small validation utility I wrote after encountering difficult atom-mapping inconsistencies during ligand parameterization. It compares atom coordinates across state-specific MOL2 files and flags atom names that map to different coordinates.

This automated a debugging step that I had previously performed manually and helped catch subtle inconsistencies before they propagated into the larger simulation workflow.

Workflow

A simplified view of the ligand-preparation pipeline is:

Generate candidate protonation states.

Obtain CGenFF parameters for each state.

Align ligand states into a common coordinate frame.

Identify the common molecular core and state-specific substituents.

Validate atom naming/mapping across states.

Renormalize charges for a multisite λ-dynamics representation.

Combine core/patch topology files and parameter files.

Build the CHARMM ligand system for downstream CpHMD simulations.

Main tools

Python

RDKit

Open Babel

NumPy / pandas

CHARMM / pyCHARMM

CGenFF

Multisite λ-dynamics

Adaptive Landscape Flattening (ALF)

Bash / HPC workflows

Repository contents

The repository reflects a research workflow rather than a standalone software package. The main Jupyter notebook contains the evolving ligand-parameterization pipeline, while the molecular and parameter files document intermediate stages of the workflow.

Some steps depend on software and Brooks Lab infrastructure that are not distributed as part of this repository, so the repository should be viewed primarily as a research code sample and workflow record, not a turnkey reproducible package.

Research output

This work contributed to a peer-reviewed Biophysical Society abstract on extending CpHMD to titratable ligands:

DOI: https://doi.org/10.1016/j.bpj.2025.11.2197

A full manuscript describing the methodology and results is in preparation.

Acknowledgments

This work was conducted through the University of Michigan Biophysics Research Experience for Undergraduates in the Brooks Lab. I am grateful to the Brooks Lab for the simulation methodology, software infrastructure, and mentorship that supported this project.
