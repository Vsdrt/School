f = {3:1}

for n in range(4, 185):
	f[n] = 0
	f[n] += f[n - 1]

	if n % 2 == 0 and n // 2 in f:
		f[n] += f[n // 2]
	
	if n % 3 == 0 and n // 3 in f:
		f[n] += f[n // 3]

	if n == 90:
		f[n] = 0

	if n in (30, 100):
		for x in range(n):
			f[x] = 0

print(f[184])
		



def f(st, en):
	if st > en or st == 90: return 0
	if st == en: return 1
	return f(st + 1, en) +  f(st * 2, en) + f(st * 3, en)

print(f(3, 30) * f(30, 100) * f(100, 184))

	