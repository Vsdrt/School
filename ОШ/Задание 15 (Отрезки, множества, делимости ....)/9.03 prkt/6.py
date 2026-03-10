def f(x, y, a):
	return (11*x - y != 53) or (x > y) or (a < x)

a = 0
while True:
	a += 1
	if all(f(x, y, a) for x in range(0, 1500) for y in range(0, 1500)):
		print(a)