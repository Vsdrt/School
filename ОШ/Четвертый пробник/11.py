from math import ceil, log2


k = 1024
i = ceil(log2(10 + 300))
id = ceil(k * i / 8)

print(131072 * id / 1024 / 1024 )