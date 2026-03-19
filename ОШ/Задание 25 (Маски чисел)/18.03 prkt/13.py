from functools import lru_cache


@lru_cache(maxsize=None)
def simple(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


@lru_cache(maxsize=None)
def divs(x):
    res = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            if simple(i):
                res.add(i)
            if simple(x // i):
                res.add(x // i)
    return sorted(res)


def arifm(x):
    k = x[1] - x[0]
    if k == 0:
        return []
    res = set()
    for i in range(len(x) - 1):
        if x[i + 1] - x[i] == k:
            res.add(True)
        else:
            res.add(False)
    return res, k


for x in range(100_000, 500_001):
    if len(divs(x)) > 3 and len(arifm(divs(x))[0]) == 1:
        print(x, len(divs(x)) * arifm(divs(x))[1])
