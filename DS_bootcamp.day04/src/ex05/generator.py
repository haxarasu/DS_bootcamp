import sys
import time
import tracemalloc

def read_file_generator(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generator.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    tracemalloc.start()
    start_time = time.time()

    for line in read_file_generator(file_path):
        pass 

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Peak memory usage =  {peak / 10**9:.6f} GB")
    print(f"User  mode time + System mode time = {end_time - start_time:.2f} seconds")