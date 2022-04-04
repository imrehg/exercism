#!/usr/bin/env bash

find . -name *_test.py -exec python -m pytest -o markers=task {} +
