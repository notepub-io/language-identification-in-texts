#!/bin/sh

conda install six=1.16.0

# Language Detection

# Polyglot.
conda install -c conda-forge -y pyicu=2.7.4
pip install 'morfessor==2.0.6'
pip install 'polyglot==16.7.4'
conda install -c conda-forge -y pycld2=0.41
pip install 'pycountry==22.1.10'

# Fasttext.
conda install -c conda-forge -y fasttext=0.9.2
