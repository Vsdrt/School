def f(x, y, a):
	return ((x**2 > 16) or (a > x)) and ((y**2 <= 81) or (a <= y))

a = -200
while True:
	a += 1
	if all(f(x, y, a) for x in range(1, 1500) for y in range(1, 1500)):
		print(a)

