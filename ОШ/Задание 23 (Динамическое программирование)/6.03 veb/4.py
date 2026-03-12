f = {3: 1}
for n in range(4, 14):
	f[n] = 0 #создаем точку
	f[n] += f[n - 1]
	if n - 2 in f:
		f[n] += f[n - 2]
	if n == 8:
		f[n] = 0

print(f[13])
