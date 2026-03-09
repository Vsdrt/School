def divs(x):
	res = set()
	for i in range(1, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)

	return sorted(res)


for x in range(550000, 560001):
	res = set(i for i in divs(x) if str(i)[-1] == "7" and i != x)

	if len(res) == 3:
		print(x, max(res))
	
