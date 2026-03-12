f = {2:1}

for n in range(3, 21):
	f[n] = 0
	f[n] += f[n - 1]

	if n%2==0 and n // 2 in f:
		f[n] += f[n // 2]

	if int(n**0.5) == n**0.5 and int(n**0.5) in f:
		f[n] += f[int(n ** 0.5)]

	if n == 11:
		f[n] = 0

print(f[20])
	
