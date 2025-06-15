import timeit 

def list_comprehension_add(emails):
    return [email for email in emails if email.split('@')[1] == 'gmail.com']


def loop_add(emails):
    result = []
    for email in emails:
        if email.split('@')[1] == 'gmail.com':
            result.append(email)
    return result


def map_add(emails):
    return list(map(lambda email: email if email.split('@')[1] == 'gmail.com' else None, emails))


def comparison(emails):
    loop_time = timeit.timeit(lambda: loop_add(emails), number=90000000)
    list_comp_time = timeit.timeit(lambda: list_comprehension_add(emails), number=90000000)
    map_time = timeit.timeit(lambda: map_add(emails), number=90000000)
    
    times = [
        ("list comprehension", list_comp_time),
        ("loop", loop_time),
        ("map", map_time)
    ]
    
    times.sort(key=lambda x: x[1])
    
    time_compare = ' vs '.join(f"{time:.6f}" for _, time in times)
    winner = times[0][0]
    
    print(f"it is better to use a {winner}")
    print(time_compare)

if __name__ == '__main__':
    emails = ['john@gmail.com',
              'james@gmail.com',
              'alice@yahoo.com',
              'anna@live.com',
              'philipp@gmail.com'] * 5
    comparison(emails)