from itertools import product

s = "qwertyno"
res = set()

for x in product(s, repeat = 7):
    a = "".join(x)

    if "qwerty" not in a and all(a.count(c) <= 2 for c in "qwertyno"):
        res.add(a)

print(len(res))
