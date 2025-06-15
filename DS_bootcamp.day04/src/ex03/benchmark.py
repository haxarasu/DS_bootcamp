from functools import reduce
import timeit
import sys

def get_input():
    if len(sys.argv) != 4:
        print("Invalid input")
        sys.exit(1)
    return sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

def loop_usage(n):
    result = 0
    for i in range (1, n+1):
        result += i*i
    return result

def reduce_usage(n):
    return reduce(lambda x, y: x + y*y, range(1, n+1))

def main():
    name, calls, n = get_input()
    if name == "loop":
        print(timeit.timeit(lambda: loop_usage(n), number=calls))
    elif name == "reduce":
        print(timeit.timeit(lambda: reduce_usage(n), number=calls))
    else:
        print("Invalid input")
        sys.exit(1)

if __name__ == "__main__":
    main()