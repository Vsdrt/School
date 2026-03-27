from math import ceil, log2

for k in range(1, 100000):
	id = ceil(23 * k / 8)
	if id * 500_000 <= 21 * 1024 * 1024:
		print(k)

print(2**15)