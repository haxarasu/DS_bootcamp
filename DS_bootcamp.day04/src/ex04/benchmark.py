import random
import timeit
from collections import Counter


def top_10_common_numbers(numbers):
    count_dict = {}
    
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    
    sorted_numbers = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)[:10]
    return dict(sorted_numbers)


def count_numbers(numbers):
    counts = {i: 0 for i in range(101)}

    for number in numbers:
        counts[number] += 1
    
    return counts


def get_dict(numbers):
    return Counter(numbers)


def get_top_10_with_common(counter):
    return counter.most_common(10)


if __name__ == "__main__":
    numbers = [random.randint(0, 100) for _ in range(1000000)]

    time_with_counter_2 = timeit.timeit(lambda: get_dict(numbers), number = 10)
    time_with_counter_3 = timeit.timeit(lambda: get_top_10_with_common(get_dict(numbers)), number = 10)

    time_without_counter_2 = timeit.timeit(lambda: count_numbers(numbers), number = 10)
    time_without_counter_3 = timeit.timeit(lambda: top_10_common_numbers(numbers), number = 10)
    

    print(f"my function: {time_without_counter_2}")
    print(f"Counter: {time_with_counter_2}")

    print(f"my top: {time_without_counter_3}")
    print(f"Counter's top: {time_with_counter_3}")