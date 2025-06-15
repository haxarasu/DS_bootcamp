#!/bin/bash

OUTPUT="hh_positions_combined.csv"

> "${OUTPUT}"

first_file=$(find . -type f -name "*.csv" | head -n 1)
head -n 1 "$first_file" >> "${OUTPUT}"

find . -type f -name "*.csv" | while IFS= read -r file; do
    tail -n +2 "$file" >> "${OUTPUT}"
done

