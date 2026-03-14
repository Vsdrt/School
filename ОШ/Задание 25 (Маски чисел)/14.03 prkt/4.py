def divs(x):
	res = set()
	for i in range(1, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)

	return sorted(res)

k = 0

for x in range(500_001, 500_200):
	deli = divs(x)
	for i in deli:
		if str(i)[-1] == "8" and i != 8 and i != x :
			print(x, i)
			