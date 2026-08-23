#!/bin/sh
#
python3 solver.py > raw.txt
python3 wrapper.py > out.txt
cat out.txt
