#!/bin/bash

# add option -v for verbose output

echo "Cleaning proyect"
rm -rf  bin etc include lib share lib* pyvenv.cfg .mypy_cache
echo "Done"
exit 0