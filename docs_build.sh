#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
mkdir -p docs/build
./venv/bin/python -m sphinx -b html docs/source docs/build/html
echo "Documentation build complete. Open docs/build/html/index.html to view."
