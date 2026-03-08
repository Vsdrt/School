from itertools import product

s = "автор"
res = set()

for x in product(s, repeat = 4):
    a = "".join(x)
    res.add(a)

k = 0
for x in sorted(res):
    k += 1
    if x == "вата":
        print(k, x)
    
