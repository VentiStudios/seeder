import random
from tqdm import trange

def find(target, min=0, max=100, max_seed=1000000, min_seed=0, direct=True):
    possible_seeds = []
    for seed in trange(min_seed, max_seed):
        random.seed(seed)
        found = True
        for _ in range(len(target)):
            if random.randint(min, max) != target[_]:
                found = False
                break
        if found:
            if direct:
                return [seed]
            possible_seeds.append(seed)
    return possible_seeds
