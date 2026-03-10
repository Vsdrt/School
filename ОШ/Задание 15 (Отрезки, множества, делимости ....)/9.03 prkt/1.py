def f(x, y, a):
	return (x + y <= 30) or (y <= x + 2) or (y >= a)

a = -1
while True:
	a += 1
	if all(f(x, y, a) for x in range(1, 1500) for y in range(1, 1500)):
		print(a)