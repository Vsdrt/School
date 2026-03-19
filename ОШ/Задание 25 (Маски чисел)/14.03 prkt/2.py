from math import prod


def divs(x):
    res = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return res


for x in range(174457, 174505):
    if len(divs(x)) == 2:
        print(sorted(divs(x)))
