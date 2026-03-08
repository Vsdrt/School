from itertools import product

cif = "0123456789"
res = set()

for k in range(5):
    for g in range(5-k):
        for a in product(cif, repeat = k):
            for b in product(cif, repeat = g):
                a = "".join(a)
                b = "".join(b)
                x = a + "15" + b + "7424"
                x = int(x)
                d1 = x%111 == 0
                d2 = x%113 == 0
                d3 = x%127 == 0
                if x <= 10**8 and (d1 + d2 + d3) == 1:
                    if d1:
                        res.add((x, x/111))
                    elif d2:
                        res.add((x, x/113))
                    else:
                        res.add((x, x/127))

for x in sorted(res):
    print(x)
                
