def f(x, a):
	return (x&a!=0) <= ((x&17==0 and x&5==0) <= (x&3!=0))

a = -1
while True:
	a += 1
	if all(f(x, a) for x in range(0, 1000000)):
		print(a)







