#!/bin/bash

python3 solver.py > data2.txt

for (( i=1; i < $1; ++i ))
do
    python3 solver.py >> data2.txt
    echo "....." >> data2.txt
done
