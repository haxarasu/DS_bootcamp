#!/bin/bash

VACANCY=$1

ENCODED_VACANCY=$(echo -n "$VACANCY" | jq -sRr @uri)

curl -s -X GET "https://api.hh.ru/vacancies?text=${ENCODED_VACANCY}&per_page=20" | jq --indent 4 '.' > hh.json