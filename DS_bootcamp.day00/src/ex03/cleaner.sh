#!/bin/sh

head -n 1 ../ex02/hh_sorted.csv > hh_positions.csv

tail -n +2 ../ex02/hh_sorted.csv | awk -F ',' '
BEGIN {
    OFS = "," 
}
{
    name = tolower($3)

    pos = "-"

    if (name ~ /junior/) pos = "Junior"
    if (name ~ /middle/) pos = (pos == "-" ? "Middle" : pos "/Middle")
    if (name ~ /senior/) pos = (pos == "-" ? "Senior" : pos "/Senior")

    print $1, $2, "\"" pos "\"", $4, $5
}' >> hh_positions.csv
