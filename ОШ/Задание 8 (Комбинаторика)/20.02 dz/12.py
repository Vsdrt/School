from itertools import product

s = "бараш"
res = set()

for x in product(s, repeat = 5):
    a = "".join(x)
    res.add(a)

print(sorted(res))

k = 0
for x in sorted(res):
    k += 1
    q = sorted(x)
    x1 = [c for c in q if q.count(c) == 1]
    x2 = [c for c in q if q.count(c) == 2]

    if x.count("б") + x.count("р") + x.count("ш") <= 3 and len(x1) == 3 and len(x2)==2:
        print(k, x, x1, x2)
