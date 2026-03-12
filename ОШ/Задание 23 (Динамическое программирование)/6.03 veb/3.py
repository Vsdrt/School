f = {2: 1}

for n in range(3, 46):
	f[n] = 0
	f[n] += f[n - 1]
	if n % 2 == 0:
		f[n] += f[n // 2]
	if n in (9, 20):
		for x in range(n):
			f[x] = 0

print(f[45])