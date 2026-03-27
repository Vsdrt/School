from math import ceil, log2

k = 196
i = ceil(log2(10 + 1550))
ID = ceil(k * i / 8)

polz = 604 * 1024 // 2048

print(polz - ID)
