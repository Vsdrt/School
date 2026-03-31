for i in range(1, 70):
	if 1024 * 1024 * (i + i // 3) <= 2 * 1024 * 1024 * 8:
		print(2**i)


