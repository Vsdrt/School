from math import ceil, log2


len = 24

for n in range(1, 10000):
	i = ceil(log2(26 * 2 + 10 + n))
	kod = ceil(len * i / 8)
	if 5100 * kod <= 170 * 1024:
		print(n)