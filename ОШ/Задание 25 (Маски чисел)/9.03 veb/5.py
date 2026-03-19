from itertools import product


def pal(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False


def divs(x):
    res = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return sorted(res)


cif = "0123456789"
res = set()

for a in cif:
    for k in range(5):
        for p in range(5 - k):
            for b in product(cif, repeat=k):
                for c in product(cif, repeat=p):
                    b = "".join(b)
                    c = "".join(c)
                    x = f"{b}2{a}2{c}"
                    x = int(x)
                    if x <= 10**7 and pal(x) and x % 53 == 0 and len(divs(x)) > 30:
                        res.add(x)

for x in sorted(res):
    print(x, sum(divs(x)))
