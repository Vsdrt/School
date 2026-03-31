def solve(x):
	a = bin(x)[2:]
	a = a + a[-1:]
	a = a + str(a.count("1")%2)
	return int(a, 2)


for n in range(1, 1000000):
	if solve(n) < 13500:
		print(solve(n))



