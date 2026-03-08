from itertools import product

s = "oeqwr"
res = set()
for x in product(s, repeat = 6):
    a = "".join(x)

    if a[0] in "oe":
        res.add(a)

print(len(res), len("qwr"))
