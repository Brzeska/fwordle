#!/bin/sh

echo "....." > data.txt

for (( i=0; i < $1; ++i ))
do
    python3 solver.py >> data.txt
    echo "....." >> data.txt
done
