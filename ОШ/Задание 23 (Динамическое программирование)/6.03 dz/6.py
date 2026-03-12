f = {1: 1}

for n in range(2, 64):
	f[n] = 0

	if n - 2 in f:
		f[n] += f[n - 2]
	
	if n%3==0 and n // 3 in f:
		f[n] += f[n // 3]
	
	if n == 6:
		f[n] = 0
	
	if n == 25:
		for x in range(n):
			f[x] = 0

print(f[63])