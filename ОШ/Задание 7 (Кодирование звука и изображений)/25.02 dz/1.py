for i in range(1, 10000):
	if 1920 * i * 1080 <= 3 * 1024 * 1024 * 8:
		print(i, 2 ** i)