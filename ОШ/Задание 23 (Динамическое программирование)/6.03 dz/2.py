f = {1:1}

for n in range(2, 14):
	f[n] = 0
	f[n] += f[n - 1]

	if n - 2 in f:
		f[n] += f[n - 2] 
	
	if n%4==0 and n // 4 in f:
		f[n] += f[n // 4]

print(f[13])