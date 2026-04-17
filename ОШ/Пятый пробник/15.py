def f(x, y, a):
	return (5 < y) or (x > 32) or (x + 2 * y < a)


a = -1
while True:
	a += 1

	if all(f(x, y, a) for x in range(1000) for y in range(1000)):
		print(a)
		break