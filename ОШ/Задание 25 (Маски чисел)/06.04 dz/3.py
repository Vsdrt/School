def divs(x):
	res = set()
	for i in range(1, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)
	return sorted(res)


for x in range(190201, 190260 + 1):
	even = [i for i in divs(x) if i%2==0]
	even.sort()

	if len(even) == 4:
		print(x, even[-1],even[-2])