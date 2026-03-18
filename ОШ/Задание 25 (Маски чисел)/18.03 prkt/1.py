def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			if str(i)[-1] == "9" and i != 9:
				res.add(i)
			if str(x//i)[-1] == "9" and x//i != 9:
				res.add(x//i)
	return sorted(res)



for x in range(800_001, 801_000):
	if len(divs(x)) >= 1:
		print(x, min(divs(x)))