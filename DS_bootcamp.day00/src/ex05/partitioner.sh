#!/bin/sh

for file in *.csv; do
    > "$file"
done

#!/bin/sh

header=$(head -n 1 ../ex03/hh_positions.csv)

rm -f *.csv

tail -n +2 ../ex03/hh_positions.csv | while IFS=, read -r id created_at name has_test alternate_url
do
    # Извлекаем дату из столбца created_at
    date=$(echo $created_at | cut -d'T' -f1)

    if [ ! -f "${date}.csv" ]; then
        echo "$header" > "${date}.csv"
    fi

    echo "$id,$created_at,$name,$has_test,$alternate_url" >> "${date}.csv"
done

