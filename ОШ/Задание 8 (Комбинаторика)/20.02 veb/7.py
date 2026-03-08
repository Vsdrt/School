from itertools import product

s = "дожс"
res = set()

for x in product(s, repeat = 6):
    a = "".join(x)
    res.add(a)

k = 0
for x in sorted(res):
    k += 1
    if x[:2] == "жс":
        print(x, k)
        break
