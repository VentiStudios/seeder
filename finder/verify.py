import random

seeds = [31030323]
result = []

for seed in seeds:
    random.seed(seed)
    for i in range(10):
        result.append(random.randint(0, 10))
    print(result)
    result = []