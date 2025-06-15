#!/bin/sh

echo "\"name\",\"count\"" > hh_uniq_positions.csv

tail -n +2 ../ex03/hh_positions.csv | awk -F ',' '
{
    # Удаляем кавычки вокруг имени
    gsub(/"/, "", $3)
    if ($3 != "-") {
        positions[$3]++
    }
} 
END {
    for (position in positions) {
        print "\"" position "\",", positions[position]
    }
}' | sort -t ',' -k2,2nr >> hh_uniq_positions.csv

