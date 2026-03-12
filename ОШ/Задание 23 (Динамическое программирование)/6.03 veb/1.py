f = {1: 1}

for n in range(2, 16):
	f[n] = 0
	f[n] += f[n - 1]
	if n - 3 in f:
		f[n] += f[n - 3]

print(f[15])