from math import ceil, log2


doc = int(1024 / 0.7) * 8 
i = int(doc / 1000)
M = 2 ** i

print(M - 48 - 150)