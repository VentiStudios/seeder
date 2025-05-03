import random

seeds = [7756316, 1474568]
result = []

for seed in seeds:
    random.seed(seed)
    for i in range(10):
        result.append(random.randint(0, 6))
    print(result)
    result = []