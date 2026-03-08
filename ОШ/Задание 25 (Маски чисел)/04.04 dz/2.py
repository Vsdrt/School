"""from fnmatch import fnmatch

s = "12345?7?8"
for x in range(0, 10**9, 23):
    if fnmatch(str(x), s):
        print(x, x//23)
        
123450798 5367426
123451718 5367466
123453788 5367556
123454708 5367596
123456778 5367686
123459768 5367816
"""
from itertools import product

cif = "0123456789"
res = set()

for a in cif:
    for b in cif:
        x = "12345" + a + "7" + b + "8"
        x = int(x)
        if x <= 10**9 and x%23==0:
            res.add(x)

for x in sorted(res):
    print(x, x//23)
