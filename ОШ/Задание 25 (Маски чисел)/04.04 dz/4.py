from itertools import product

cif = "0123456789"
res = set()

for a in cif:
    for b in cif:
        for k in range(6):
            for c in product(cif, repeat = k):
                c = "".join(c)
                x = "12" + a + b + "36" + c + "1"
                x = int(x)
                if x <= 10**8 and x%273==0:
                    res.add(x)

for x in sorted(res):
    print(x, x//273)
