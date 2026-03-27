from math import ceil, log2

len = 21
i = ceil(log2(7))

password = ceil(len * i / 8)

print(40 * password)