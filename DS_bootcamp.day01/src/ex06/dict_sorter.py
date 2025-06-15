def tuples_to_dictionary(list_of_tuples):
    result_dict = {}

    for key, value in list_of_tuples:
        if value not in result_dict:
            result_dict[value] = []  
        result_dict[value].append(key) 
    return result_dict
    

def sorted_dictionary(unsorted_dict):
    return sorted(unsorted_dict.items(), key = lambda item: int(item[0]), reverse = True)


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

    dict_sorted = sorted_dictionary(tuples_to_dictionary(list_of_tuples))
    for key, value in dict_sorted:
        for country in sorted(value):
            print(country)