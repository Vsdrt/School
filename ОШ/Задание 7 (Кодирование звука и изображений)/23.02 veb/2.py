for T in range(1, 1000000):
	if T * 2 * 44000 * 24 <= 167 * 1024 * 1024 * 8:
		print(int(T/60))