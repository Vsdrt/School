from math  import ceil


for i in range(1, 10000):
	if ceil(2 * 48 * 1000 * (4 * 60 + 5) * i) <= 46 * 1024 * 1024 * 8:
		print(i)
