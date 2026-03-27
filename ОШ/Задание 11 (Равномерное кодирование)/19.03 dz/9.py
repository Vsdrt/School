from math import ceil, log2


len = 53

for x in range(1, 10000):
	i = ceil(log2(10 + 52 + x))
	nom = ceil(i * len / 8)
	if 2000 * nom <= 93 * 1024:
		print(x)