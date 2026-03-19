from functools import *


@lru_cache(None)
def divs(x):
    res = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return sorted(res)


for i in range(700_001, 723543415434534534500):
    x = (i, i + 1, i + 2, i + 3, i + 4)
    if (
        len(divs(x[4]))
        > len(divs(x[3]))
        > len(divs(x[2]))
        > len(divs(x[1]))
        > len(divs(x[0]))
    ):
        for p in x:
            print(p, len(divs(p)))
        break
