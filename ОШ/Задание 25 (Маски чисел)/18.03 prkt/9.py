from itertools import product
from fnmatch import fnmatch

cif = "0123456789"
s = "2?1*67"

for x in range(1, 10**7):
    if x % 159 == 0 and fnmatch(str(x), s):
        print(x, x // 159)
