from itertools import product

cif = "0123456789"
res = set()

for b in cif:
    for k in range(5):
        for a in product(cif, repeat = k):
            a = "".join(a)
            x = "2" + a + '5443' + b + '1'
            x = int(x)
            if x <= 10**8 and x%23==0:
                res.add(x)

for x in sorted(res):
    print(x, x//23)

