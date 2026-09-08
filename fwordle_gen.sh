#!/bin/bash

python3 fwordle_gen.py > raw.txt
python3 wrapper.py > out.txt
cat out.txt
