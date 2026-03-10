def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			if simple(i):
				res.add(i)
			if simple(x//i):
				res.add(x//i)
	return sum(res)



def simple(x):
	if x == 0 or x == 1:
		return False
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			return False
	return True


k = 0 
for x in range(250_001, 2000000000000):
	s = divs(x)
	if s != 0 and s%17 == 0 and k <= 4:
		print(x, s)
		k += 1