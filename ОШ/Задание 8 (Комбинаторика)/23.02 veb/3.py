from itertools import product

s = "аклмня"
res = set()
for x in product(s, repeat = 5):
    a = "".join(x)
    res.add(a)

k = 0
for x in sorted(res):
    if x[0] == "м" and x[1] == "н":
        k += 1

print(k - 2)
    
