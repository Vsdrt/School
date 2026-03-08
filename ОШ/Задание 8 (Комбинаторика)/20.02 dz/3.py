from itertools import product

s = "krant"
res = set()

for x in product(s, repeat = 5):
    a = "".join(x)

    if a.count("k") == 2:
        res.add(a)

print(len(res), res)
