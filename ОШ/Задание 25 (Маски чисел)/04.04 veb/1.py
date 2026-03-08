from itertools import product


cif = "0123456789"
res = set()

for a in cif:
    for k in range(4):
        for b in product(cif, repeat = k):
            b = "".join(b)
            x = "1" + a + "2157" + b + "4"
            x = int(x)
            if x <= 10**10 and x%2024 == 0:
                res.add(x)

for x in sorted(res):
    print(x, x//2024)
