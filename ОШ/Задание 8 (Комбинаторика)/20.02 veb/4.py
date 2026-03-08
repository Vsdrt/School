from itertools import product

s = "vasyvasy"
res = set()

for x in product(s, repeat = 5):
    a = "".join(x)
    if a.count("a") >= 1:
        res.add(a)

print(len(res))




