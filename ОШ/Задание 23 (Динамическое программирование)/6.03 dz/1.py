f = {5:1}

for n in range(6, 50):
	f[n] = 0
	f[n] += f[n - 1]

	if n%3==0 and n // 3 in f:
		f[n] += f[n // 3]

print(f)