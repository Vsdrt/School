from itertools import product

cif_ch = "02468"
cif_nch = "13579"
res = set()


for a in cif_ch:
    for k in range(6):
        for b in product(cif_nch, repeat = k):
            b = "".join(b)
            x = "1" + a + "2157" + b + "4"
            x = int(x)
            if x <= 10**10 and x%133==0:
                res.add(x)

for x in sorted(res):
    print(x, x//133)
