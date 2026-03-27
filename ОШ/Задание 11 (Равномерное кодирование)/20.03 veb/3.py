from math import ceil, log2

k = 244
i = ceil(log2(1550 + 10))
id = ceil(k * i / 8)

print(id * 32768 // 1024 )