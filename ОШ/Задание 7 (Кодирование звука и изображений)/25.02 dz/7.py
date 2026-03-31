I = 4 * 20 * 60 * 192_000 * 24 

for k in range(1, 10000):
	if (I / k) / 12_800 == 10 * 60:
		print(k)