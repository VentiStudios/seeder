import random
from multiprocessing import Pool, cpu_count, freeze_support
from tqdm import tqdm

def process_seed(args):
        seed, number, count, min_val, max_val = args
        rng = random.Random(seed)
        found = all(rng.randint(min_val, max_val) == number for _ in range(count))
        return seed if found else None

def find(number: int, count: int, max_count=1, 
                 min_val=0, max_val=100, max_seed=1_000_000,
                 min_seed=0, direct=True, processes=cpu_count() // 2) -> list[int]:

    def _worker():
        seeds = range(min_seed, max_seed)
        with Pool(processes=processes) as pool:
            with tqdm(total=len(seeds), desc="种子搜索进度") as pbar:
                results = []
                for result in pool.imap_unordered(
                    process_seed,
                    ((s, number, count, min_val, max_val) for s in seeds),
                    chunksize=1000
                ):
                    if result is not None:
                        results.append(result)
                        if direct and len(results) >= max_count:
                            pool.terminate()
                            break
                    pbar.update(1)
        return results[:max_count] if direct else results

    # macOS/Windows特殊处理
    if __name__ == '__main__':
        freeze_support()
        return _worker()
    return _worker()

def process_seed_special(args):
        seed, array, min_val, max_val = args
        rng = random.Random(seed)
        found = all(rng.randint(min_val, max_val) == _ for _ in array)
        return seed if found else None

def find_special(array: list[int], max_count=1, 
                 min_val=0, max_val=100, max_seed=1_000_000,
                 min_seed=0, direct=True, threads=cpu_count() // 2) -> list[int]:

    def _worker():
        seeds = range(min_seed, max_seed)
        with Pool(processes=threads) as pool:
            with tqdm(total=max_seed, initial=min_seed, desc="种子搜索进度") as pbar:
                results = []
                for result in pool.imap_unordered(
                    process_seed_special,
                    ((s, array, min_val, max_val) for s in seeds),
                    chunksize=1000
                ):
                    if result is not None:
                        results.append(result)
                        if direct and len(results) >= max_count:
                            pool.terminate()
                            break
                    pbar.update(1)
        return results[:max_count] if direct else results

    # macOS/Windows特殊处理
    if __name__ == '__main__':
        freeze_support()
        return _worker()
    return _worker()