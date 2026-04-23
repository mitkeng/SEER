#!/bin/bash
# 1. Install uv for high-speed dependency management
pip install uv -q

# 2. Install core Python dependencies directly via uv
# Note: protobuf 6.31.1 is required specifically for YDF compatibility in this environment
uv pip install --system -q \
    rdkit \
    tensorflow_decision_forests \
    trainer \
    ase \
    py3Dmol \
    openbabel-wheel \
    bidict \
    mlatom \
    torchani \
    pymol-open-source \
    ydf \
    chemml \
    e3nn \
    pandas \
    numpy \
    pytz \
    "protobuf==6.31.1"

# 3. Setup Condacolab for PyMOL bundle
pip install -q condacolab
python -c "import condacolab; condacolab.install()"

# Note: This script triggers a kernel restart.
# After restart, run the Mamba command in the user guide.
