from main_optimized import *

if __name__ == "__main__":
    print(find_special(array=[1, 1, 4, 5, 1, 4, 1, 9, 1, 9, 8, 1, 0], max_count=1, min_val=0, max_val=9, max_seed=10**13, 
                       min_seed=2067398815, threads=4))