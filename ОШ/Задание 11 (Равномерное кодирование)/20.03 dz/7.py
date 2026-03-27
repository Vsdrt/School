from math import ceil, log2


for k in range(1, 1000):
	id = ceil(k * log2(10 + 26 + 476) / 8)

	if id * 5000 <= 1024 * 1024 * 1:
		print(k)

