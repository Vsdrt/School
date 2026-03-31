for i in range(1, 100):
	if (192 * 960 * i) * 0.65 <= 90 * 1024 * 8:
		print(2**i)