f = {3:1}

for n in range(4, 22):
	f[n] = 0
	f[n] += f[n - 1]

	if n - 3 in f:
		f[n] += f[n - 3]

	if n%2==0 and n // 2 in f:
		f[n] += f[n // 2]

	if n in (8, ):
		for x in range(n):
			f[x] = 0
	
	if n == 12:
		f[n] = 0

		
print(f[21])