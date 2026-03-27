from math import ceil, log2


id = ceil(102 * ceil(log2(510 + 10)) / 8)

print(7 * 1024 * 1024 // id)