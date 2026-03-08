def solve(x):
	a = bin(x)[2:]
	if a.count("1")%2==0:
		a = "1" + a[2:] + "0"
	else:
		a = "11" + a[2:] + "1"

	return int(a, 2)



for n in range(1, 10000):
	if solve(n) > 25:
		print(n, solve(n))


	
