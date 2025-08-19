#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR
cd ..
bash scripts/get-test-data.sh
mkdir -p dist
mkdir -p testout
rm dist/*
rm testout/*
python3 -m build
pip install --force-reinstall --no-deps dist/planktofeatures*.whl
python3 scripts/test.py
