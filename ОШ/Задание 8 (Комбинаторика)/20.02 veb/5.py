from itertools import product

s = "maslo"
res = set()

for x in product(s, repeat = 6):
    a = "".join(x)

    if sum(a.count(c) for c in "ao") == 1:
        res.add(a)

print(len(res))
        
