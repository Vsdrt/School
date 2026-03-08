def f(x, y, a):
	return (x > a) or (y > a) or ((y - 2*x + 12) != 0)

a = -1
while True:
	a += 1
	if all(f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)):
		print(a)