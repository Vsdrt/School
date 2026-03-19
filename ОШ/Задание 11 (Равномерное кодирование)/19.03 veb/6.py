from math import log2, ceil 


k = 261

for i in range(1, 20):
	ID = ceil(k * i / 8)
	if ID * 252_500 > 31 * 1024 * 1024:
		break

for N in range(1, 16):
	if ceil(log2(N)) == i:
		print(N)
		break