#!/bin/sh

> hh.csv

echo "id,created_at,name,has_test,alternate_url" > "hh.csv"

jq -r -f "filter.jq" "../ex00/hh.json" >> "hh.csv"

