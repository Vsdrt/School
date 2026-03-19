from math import log2


N = 8
k = 35

i = int(log2(N))
ID = int((k * i) / 8) + 1

print((ID * 21504)//2**10)