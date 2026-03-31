for i in range(1, 10000):
	I = 1920 * 1080 * i / 8 / 1024 / 1024
	paket = I * 30 + 3
	if paket / 1 <= 3 * 60:
		print(2 ** i) 
