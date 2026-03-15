def solve(x):
	a = bin(x)[2:]
	a = a + a[-2]
	a = a + a[1]
	return int(a, 2)

for n in range(10, 1000):
	if solve(n) <= 128:
		print(n, solve(n))