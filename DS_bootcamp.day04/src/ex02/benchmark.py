import timeit 
import sys

def list_comprehension_add(emails):
    return [email for email in emails if email.split('@')[1] == 'gmail.com']


def loop_add(emails):
    result = []
    for email in emails:
        if email.split('@')[1] == 'gmail.com':
            result.append(email)
    return result


def filter_add(emails):
    return list(filter(lambda email: email.split('@')[1] == 'gmail.com', emails))


def map_add(emails):
    return list(map(lambda email: email if email.split('@')[1] == 'gmail.com' else None, emails))


def get_input():
    if len(sys.argv) == 3:
        method = sys.argv[1]
        count = sys.argv[2]
        return method, count
    else:
        raise ValueError('Invalid input')
        

if __name__ == '__main__':
    emails = ['john@gmail.com',
              'james@gmail.com',
              'alice@yahoo.com',
              'anna@live.com',
              'philipp@gmail.com'] * 5
    
    method, count = get_input()

    try:
        count = int(count)
    except ValueError:
        raise ValueError('Invalid input')

    if method == 'list_comprehension':
        print(timeit.timeit(lambda: list_comprehension_add(emails), number = int(count)))
    elif method == 'loop':
        print(timeit.timeit(lambda: loop_add(emails), number = int(count)))
    elif method == 'filter':
        print(timeit.timeit(lambda: filter_add(emails), number = int(count)))
    elif method == 'map':
        print(timeit.timeit(lambda: map_add(emails), number = int(count)))
    else:
        raise ValueError('Invalid input')