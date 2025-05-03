from main_optimized import *
import time

if __name__ == "__main__":
    before = time.time()
    print(find(number=0, count=9, max_count=2, min_val=0, max_val=10, max_seed=2147483647, min_seed=0))
    print(time.time() - before)