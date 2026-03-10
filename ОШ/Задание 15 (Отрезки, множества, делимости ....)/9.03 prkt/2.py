def f(x, a):
	return (x%18==0) <= ((x%54==0) <= (x%a==0))

a = 0
while True:
	a += 1
	if all(f(x//4, a) for x in range(4, 8000)):
		print(a)