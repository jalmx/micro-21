#!/bin/bash

python3 -m venv .
source ./bin/activate
pip install notebook
pip install autopep8
pip install beautifulsoup4 request
jupyter notebook ./book