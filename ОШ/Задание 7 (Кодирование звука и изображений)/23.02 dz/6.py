for t in range(1, 100000):
	if 2 * 48000 * 24 * t <= 5625 * 1024 * 1024 * 8:
		if int(t/60)%5 == 0:
			print(int(t/60))