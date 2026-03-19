from math import log2

N = 4090 + 10
k = 317

i = int(log2(N)) + 1
ID = int((k * i) / 8) + 1

print((262144 * ID) // 2**10 // 2**10)
