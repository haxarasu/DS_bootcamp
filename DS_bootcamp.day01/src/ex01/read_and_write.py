def convert_csv_to_tsv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        with open(output_file, 'w', encoding='utf-8') as tsv_file:
            inside_quotes = False
            for line in csv_file:
                new_line = []
                for char in line:
                    if char == '"':
                        inside_quotes = not inside_quotes  # Меняем состояние при встрече кавычки
                    if char == ',' and not inside_quotes:
                        new_line.append('\t')  # Заменяем запятую на табуляцию, если не внутри кавычек
                    else:
                        new_line.append(char)
                tsv_file.write(''.join(new_line))  # Записываем измененную строку в TSV файл

if __name__ == '__main__':
    convert_csv_to_tsv('ds.csv', 'ds.tsv')