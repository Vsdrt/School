from math import ceil


for i in range(1, 1000):
	if ceil(2 * 44000 * (5 * 60 + 25) * i) <= 82 * 1024 * 1024 * 8:
		print(i)