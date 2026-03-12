f = {3:1}

for n in range(4, 21):
	f[n] = 0
	f[n] += f[n - 1]

	if n - 3 in f:
		f[n] += f[n - 3]

	if n%2==0 and n//2 in f:
		f[n] += f[n // 2]

	if n in (9, 12):
		for x in range(n):
			f[x] = 0

print(f[20])