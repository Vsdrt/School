from math import ceil, log2

k = 24
i = ceil(log2(10 + 60))
id = ceil(k * i / 8)

ip = 4

polz = 70 * 1024 // 2048
print(polz - id - ip)