from math import ceil, log2

len = 11
i = ceil(log2(10 + 12 + 12))

password = ceil(len * i / 8)

print(60 * password)