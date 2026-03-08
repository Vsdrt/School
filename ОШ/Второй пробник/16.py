def f(n, x):
	if n >= 3000:
		return n
	else:
		return n + x + f(n+2, x)
	

for x in range(-1000, 1000):
	if f(2984, x) - f(2988, x) == 5916:
		print(x)
