from itertools import product


def nc_divs(x):
    res = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            if i % 2 != 0:
                res.add(i)
            if (x // i) % 2 != 0:
                res.add(x // i)
    return sorted(res)


cif = "0123456789"
res = set()

for a in cif:
    for k in range(5):
        for b in product(cif, repeat=k):
            b = "".join(b)
            x = f"14{a}4{b}"
            x = int(x)
            if x < 10**7 and x % 217 == 0:
                res.add(x)

for x in sorted(res)[-7:]:
    print(x, sum(nc_divs(x)))
