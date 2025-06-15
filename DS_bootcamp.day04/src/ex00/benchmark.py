import timeit 

def list_comprehension_add(emails):
    return [email for email in emails if email.split('@')[1] == 'gmail.com']


def cylic_add(emails):
    result = []
    for email in emails:
        if email.split('@')[1] == 'gmail.com':
            result.append(email)
    return result
    

def comparison(emails):
    loop_time = timeit.timeit(lambda: cylic_add(emails), number = 90000000)
    list_comp_time = timeit.timeit(lambda: list_comprehension_add(emails), number = 90000000)
    
    if list_comp_time <= loop_time:
        print("it is better to use a list comprehension")
        time_compare = f'{list_comp_time} vs {loop_time}'
        print(time_compare)
    else:
        print("it is better to use a cycle")
        time_compare = f'{loop_time} vs {list_comp_time}'
        print(time_compare)
    

if __name__ == '__main__':
    emails = ['john@gmail.com',
              'james@gmail.com',
              'alice@yahoo.com',
              'anna@live.com',
              'philipp@gmail.com'] * 5
    comparison(emails)