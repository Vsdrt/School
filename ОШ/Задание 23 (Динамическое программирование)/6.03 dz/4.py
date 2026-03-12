f = {1:1}

for n in range(2, 31):
	f[n] = 0
	f[n] += f[n - 1]

	if n % 2==0 and n // 2 in f:
		f[n] += f[n // 2]

	if n == 10:
		f[n] = 0

print(f[30])