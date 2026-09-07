#!/usr/bin/env bash
# Everything needed to build and check this repository:
#   - CadQuery, for the model, the motion planner and the collision checker
#   - ruff, the Python static checker
#   - markdownlint-cli2, the Markdown static checker
#
# The documentation site needs nothing here: actions/jekyll-build-pages brings
# its own github-pages gem set.
set -euo pipefail

# OpenCascade, which CadQuery wraps, needs these system libraries at import time.
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
  libgl1 libglu1-mesa libxi6 libxrender1 libxcursor1 libxft2 libxinerama1 \
  build-essential

python -m pip install --upgrade pip

# CadQuery, pinned by cad/requirements.txt; the wheels carry the OpenCascade kernel.
python -m pip install -r cad/requirements.txt

python -m pip install ruff

sudo npm install --global markdownlint-cli2@0.23.2

# Prove the OpenCascade kernel actually loads, not just that the wheel unpacked.
python -c "import cadquery; print('cadquery', cadquery.__version__)"
python -c "import cadquery as cq; print('kernel ok, test volume', cq.Workplane('XY').box(1,1,1).val().Volume())"
ruff --version
markdownlint-cli2 --version
