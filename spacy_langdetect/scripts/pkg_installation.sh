#!/bin/sh

conda install -c conda-forge spacy=3.2.1
pip install spacy_langdetect
pip install 'pycountry==22.1.10'
python -m spacy download en_core_web_sm