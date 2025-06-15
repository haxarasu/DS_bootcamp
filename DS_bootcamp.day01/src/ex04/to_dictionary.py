def tuples_to_dictionary(list_of_tuples):
    result_dict = {}

    for country, number in list_of_tuples:
        if number not in result_dict:
            result_dict[number] = []  # Инициализируем список, если ключа еще нет
        result_dict[number].append(country)  # Добавляем страну в список значений

    return result_dict

def print_dictionary(dictionary):
    for key in dictionary:
        for value in dictionary[key]:
            print(f"'{key}' : '{value}'")

if __name__ == '__main__':
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]

    # Преобразуем список кортежей в словарь
    country_dict = tuples_to_dictionary(list_of_tuples)

    # Выводим содержимое словаря
    print_dictionary(country_dict)