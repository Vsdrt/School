from functools import lru_cache
import time


@lru_cache(maxsize=None)
def divs(x):
    res = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return res


start = time.time()

k = 0

for i in range(700_001, 231354354):
    x = (i, i + 1, i + 2, i + 3, i + 4)

    if all(len(divs(x[p])) < len(divs(x[p + 1])) for p in range(len(x) - 1)):
        for i in x:
            print(i, len(divs(i)))
        break

print(time.time() - start)
