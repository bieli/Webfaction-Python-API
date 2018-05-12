#!/usr/bin/env bash

python -m unittest discover ./tests/ "*test.py"
nosetests tests -v --with-coverage
python -m pyflakes
