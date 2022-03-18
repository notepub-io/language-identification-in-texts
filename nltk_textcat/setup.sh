#!/bin/sh

# Make scripts directory files executable.
chmod +x scripts/*

source scripts/conda_env_setup.sh
source scripts/pkg_installation.sh
