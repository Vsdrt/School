from itertools import product


def divs(x):
    res = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return sum(res)


cif = "0123456789"
cf = "123456789"
res = set()

k = 0
for a in cf:
    for d in cif:
        for k in range(3):
            for p in range(3):
                for b in product(cif, repeat=k):
                    for c in product(cif, repeat=p):
                        b = "".join(b)
                        c = "".join(c)
                        x = f"{a}6{b}6{c}{d}6"
                        x = int(x)
                        if x % 6 == 0 and x % 7 == 0 and x % 8 == 0:
                            res.add(x)

for x in sorted(res)[:7]:
    print(x, divs(x))
