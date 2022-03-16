#!/bin/sh

ENV_NAME="venv_langdetect"

export CONDA_ALWAYS_YES="true"

# Upgrade Conda
conda update -n base -c defaults conda

# Remove if environment already exists.
conda remove -n $ENV_NAME --all

# Create Environment
conda create -n $ENV_NAME python=3.8 -y

# Configure shell for conda
conda init bash

# Activate Environment
conda activate $ENV_NAME

# Disable yes to all
unset CONDA_ALWAYS_YES


