from math import log2


img = 1024 * 768 * log2(4096)

for k in range(1, 100000):
	if (img * k) / 1_310_720 <= 300:
		print(k)