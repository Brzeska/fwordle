#!/bin/sh

python3 solver.py > data.txt

for (( i=1; i < $1; ++i ))
do
    python3 solver.py >> data.txt
    echo "....." >> data.txt
done
