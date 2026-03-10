def f(x, a):
	return ((a%5==0) and ((2020%a!=0) <= (x%1718==0 <= 2023%a==0)))


a = 0 
while True:
	a += 1
	if all(f(x, a) for x in range(1, 1000000)):
		print(a)