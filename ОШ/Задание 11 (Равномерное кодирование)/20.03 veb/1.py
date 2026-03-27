from math import ceil, log2

i = ceil(log2(10 + 1024))

for k in range(1, 1000000):
	ID = ceil(i * k / 8)
	if 256 * ID < 6 * 1024:
		print(k)