def solve(x):
	a = bin(x)[2:]
	a = a + str(a.count("1")%2)
	a = a + str(a.count("1")%2)
	return int(a, 2)



for n in range(1, 1000):
	if solve(n) > 80 and solve(n) < 150:
		print(solve(n))