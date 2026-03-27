from math import ceil, log2


for k in range(1, 10000):
	id = ceil(k * ceil(log2(10 + 60)) / 8)
	if id * 999 >= 88 * 1024:
		print(k)
		break
