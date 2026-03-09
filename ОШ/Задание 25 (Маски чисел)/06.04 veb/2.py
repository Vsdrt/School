def divs(x):
	res = set()
	for  i in range(2, int(x**0.5)):
		if x%i==0:
			res.add(i)
			res.add(x//i)

	return sorted(res)

k = 0
for x in range(800_001, 801_000):
	if len(divs(x)) >= 1 and (max(divs(x)) + min(divs(x)))%138==0 and k <= 4:
		k += 1
		print(x, max(divs(x)) + min(divs(x)))
