def f(x):
	a = bin(x)[2:]

	if a.count("1")%2 == 0:
		a = "10" + a[2:] + "0"
	else:
		a = "11" + a[2:] + "1"

	
	return int(a, 2)


print(f(6), f(4))

for n in range(1, 100000):
	if f(n) > 480:
		print(n)
		break