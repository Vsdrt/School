def f(x, y, a):
	return (x > 7) or (y > 4) or (x**2 + 3 * y < a)


a = -1

while True:
	a += 1
	if all(f(x, y, a) for x in range(1000) for y in range(1000)):
		print(a)
		break