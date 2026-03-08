from itertools import product


cif = "0123456789"
cif_ch = "02468"
res = set()

for a in cif_ch:
    for k in range(7):
        for b in product(cif, repeat = k):
            b = "".join(b)
            x = a + "136" + b
            x = int(x)
            if len(b)!=0 and int(b)%2!=0 and x <= 10**10 and x%53191 == 0:
                res.add(x)

for x in sorted(res):
    print(x, x//53191)
