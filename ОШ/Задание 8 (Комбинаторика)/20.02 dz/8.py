from itertools import product

s = "гафний"
res = set()

for x in product(s, repeat = 4):
    a = "".join(x)
    
    if a[0] != "й" and ("а" in a or "и" in a):
        res.add(a)

print(len(res), res)
