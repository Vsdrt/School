from itertools import product

s = "0123456"
ch = "0246"
nch = "135"
res = set()
for x in product(s, repeat = 6):
    a = "".join(x)

    if a.count("6") == 1 and a[0] != "0" and\
       ((a[0] in ch and a[1] in nch and a[2] in ch and a[3] in nch and a[4] in ch and a[5] in nch) or \
       (a[0] in nch and a[1] in ch and a[2] in nch and a[3] in ch and a[4] in nch and a[5] in ch)):
        res.add(a)

print(len(res), res)
    
