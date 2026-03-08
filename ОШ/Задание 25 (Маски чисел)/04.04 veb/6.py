from itertools import product

cif = "0123456789"
res = set()

for b in cif:
    for k in range(4):
        for a in product(cif, repeat = k):
            a = "".join(a)
            x = "13" + a + "57" + b + "9"
            x = int(x)
            if x <= 10**9 and x%999==0:
                res.add(x)

for x in sorted(res):
    print(x, x//999)
