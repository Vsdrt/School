from itertools import product

s = "щрюи"
res = set()
for x in product(s, repeat = 5):
    a = "".join(x)
    res.add(a)


k = 0
for x in sorted(res):
    k += 1
    if x[0] == "щ" and x[-1] == "и":
        print(k, x )
