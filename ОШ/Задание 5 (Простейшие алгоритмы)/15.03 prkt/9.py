def per(x, n):
	s = ""
	while x > 0:
		s = str(x%n) + s
		x //= n
	return s


def sm(x):
	x = str(x)
	sm = 0
	for i in x:
		sm += int(i, 3)
	return sm

def solve(n):
	a = per(n, 3)
	if n % 2 == 0:
		a = "1" + a + "00"
	else:
		a = a + per(sm(a), 3)
	
	return int(a ,3)

for n in range(1, 10000):
	if solve(n) > 168:
		print(n)
		break