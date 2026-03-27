from math import ceil, log2

len = 11
i = ceil(log2(26 * 2 + 10))
password = ceil(len * i / 8)

dop = 13

polz = password + dop

print(2**10 // polz)