from itertools import product

s = "kater"
res = set()

for x in product(s, repeat = 3):
    a = "".join(x)

    if a.count("r") >= 2:
        res.add(a)

print(len(res), res)
