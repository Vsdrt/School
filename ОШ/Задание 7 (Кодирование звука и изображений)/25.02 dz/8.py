from math import log2


I = log2(8192) * 1024 * 960 

for k in range(1, 1000000):
	if k <= 280 * 1_474_560 / I:
		print(k)