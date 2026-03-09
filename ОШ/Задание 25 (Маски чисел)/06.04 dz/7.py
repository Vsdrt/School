def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)

	return sorted(res)




for x in range(400_000_001, 400_001_000):
	
	if len(divs(x)) >= 7:
		d = divs(x)[-7]
	else:
		d = 0
	
	if d > 0:
		print(d, len(divs(x)))