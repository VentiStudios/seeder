import random
from tqdm import trange, tqdm
import threading
from queue import Queue
import time

def find(number: int, count: int, max_count = 1, min_val=0, max_val=100, max_seed=1000000, min_seed=0, direct=True) -> list[int]:
    possible_seeds = []
    for seed in trange(min_seed, max_seed):
        random.seed(seed)
        found = True
        for _ in range(count):
            if random.randint(min_val, max_val) != number:
                found = False
                break
        if found:
            if random.randint(min_val, max_val) != number:
                possible_seeds.append(seed)
                if direct and len(possible_seeds) == max_count:
                    return possible_seeds
            else:
                print(f"找到了解{seed}，但连续元素个数超过了{count}")
            
    return possible_seeds
