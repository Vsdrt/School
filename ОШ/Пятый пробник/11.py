from math import log2, ceil


len = 257

for i in range(1, 10000):
	if ceil(i * 257 / 8) * 295_740 <= 33 * 1024 * 1024:
		print(i, 2**i)

