from math import ceil, log2


i = ceil(log2(10 + 1234))

for len in range(1, 1000):
	ID = ceil(i * len / 8)
	if 65536 * ID <= 2050 * 1024:
		print(len)