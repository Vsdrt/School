def solve(x):
	a = bin(x)[2:]

	for x in range(3):
		if a.count("0") == a.count("1"):
			a = a + a[-1]
		else:
			if a.count("0") < a.count("1"):
				a = a + "0"
			else:
				a = a + "1"

	return int(a, 2)

	

for n in range(2, 500):
	if solve(n)%4==0 and solve(n)%8!=0:
		print(n)