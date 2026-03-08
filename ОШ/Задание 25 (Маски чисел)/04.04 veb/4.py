"""
from fnmatch import fnmatch

s = "123?4*5679"

for x in range(0, 10**12+1, 4013):
    if fnmatch(str(x), s):
        print(x, x//4013)

"""

from itertools import product


cif = "0123456789"
res = set()

for a in cif:
    for k in range(5):
        for b in product(cif, repeat = k):
            b = "".join(b)
            x = "123" + a + "4" + b + "5679"
            x = int(x)
            if x <= 10**12 and x%4013==0:
                res.add(x)

for x in sorted(res):
    print(x, x//4013)
