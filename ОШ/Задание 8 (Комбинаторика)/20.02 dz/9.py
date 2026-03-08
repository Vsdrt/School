from itertools import product

s = "пятьдней"
res = set()

for x in product(s, repeat = 4):
    a = "".join(x)
    res.add(a)

k = 0

for x in sorted(res):
    k += 1
    if ("я" not in x) and ("е" not in x) and (len(set(x)) == len(x)):
        print(k, x)
