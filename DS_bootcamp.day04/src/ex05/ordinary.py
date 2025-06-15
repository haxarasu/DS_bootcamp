import sys
import time
import tracemalloc

def read_file_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python usual.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    tracemalloc.start()
    start_time = time.time()

    lines = read_file_to_list(file_path)

    for line in lines:
        pass

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Peak memory usage = {peak / 10**9:.6f} GB")
    print(f"User  mode time + System mode time = {end_time - start_time:.2f} seconds")