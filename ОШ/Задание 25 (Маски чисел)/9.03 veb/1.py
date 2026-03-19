from itertools import product

cif = "0123456789"
res = set()

for a in cif:
    for c in cif:
        for d in cif:
            for k in range(4):
                for b in product(cif, repeat=k):
                    b = "".join(b)
                    x = "12" + a + "3" + b + "456" + c + d + "9"
                    x = int(x)
                    if x <= 10**12 and x % 98591 == 0:
                        res.add(x)
for x in sorted(res):
    print(x, x // 98591)
