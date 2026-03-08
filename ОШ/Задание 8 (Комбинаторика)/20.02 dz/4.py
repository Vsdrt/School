from itertools import product

s = "timahevsk"
res = set()

for x in product(s, repeat = 4):
    a = "".join(x)

    if a[0] not in "iaeh":
        res.add(a)

print(len(res))
