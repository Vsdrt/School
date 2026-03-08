from itertools import product


cif = "0123456789"
res = set()

for a in cif:
    for k in range(5):
        for b in product(cif, repeat = k):
            b = "".join(b)
            x = "32" + a + "056" + b +"6"
            x = int(x)
            if x <= 10**10 and x%2023 == 0:
                res.add(x)

for x in sorted(res):
    print(x, x//2023)
