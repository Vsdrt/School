from math import ceil, log2

k = 1000
i = ceil(log2(12 + 31415))
id = ceil(k * i / 8)

print(id * 8192 // 1024)
