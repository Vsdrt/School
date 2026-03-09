def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)

	return sorted(res)


for x in range(150_001, 151_000):
	s = sum(divs(x))

	if s%13==10:
		print(x, s)
	 
