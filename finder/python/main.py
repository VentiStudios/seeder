import random
for seed in range(2147483647):
    print(f"正在测试 {seed}", end="\r")
    random.seed(seed)
    if all(random.randint(1,100) == 1 for _ in range(7)):
        print(f"\n有效种子: {seed}")