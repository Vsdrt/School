def per(x):
	s = ""
	while x > 0:
		s = str(x%6) + s
		x //= 6
	
	return s


def solve(n):
	a = per(n)
	a = a + a[-1]
	a = int(a, 6)
	a = bin(a)[2:]
	a = a + a[-1]
	return int(a, 2)


for n in range(1, 10000):
	if solve(n) < 344:
		print(solve(n))