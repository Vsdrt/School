from itertools import product

s = "грант"
s = sorted(s)
k = 0
for x in product(s, repeat = 6):
    a = "".join(x)
    k += 1
    if a == "гранат":
        print(k, a)
