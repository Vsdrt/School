def solve(x):
	a = bin(x)[2:]
	a = a + a[-1]

	if a.count("1")%2==0:
		a = a + "0"
	else:
		a = a + "1"

	if a.count("1")%2==0:
		a = a + "0"
	else:
		a = a + "1"
	
	return int(a ,2)



for n in range(1, 1_000_000):
	if solve(n) > 97 and solve(n) < 190:
		print(n, solve(n))
