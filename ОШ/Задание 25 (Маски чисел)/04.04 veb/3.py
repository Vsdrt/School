from itertools import product

cif = "0123456789"
res = set()

for a in cif:
    for b in cif:
        for k in range(5):
            for c in product(cif, repeat = k):
                c = "".join(c)
                x = "3" + a + "99" + b + "7" + c + "8"
                x = int(x)
                if x <= 10**8 and x%3226 == 0:
                    res.add(x)

for x in sorted(res):
    print(x, x//3226)

print("-"*60)

from fnmatch import fnmatch

s = "3?99?7*8"
for x in range(0, 10**8, 3226):
    if fnmatch(str(x), s):
        print(x, x//3226)
