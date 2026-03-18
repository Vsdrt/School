def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i == 0:
			res.add(i)
			res.add(x//i)
	return sorted(res)


k = 0

for x in range(250_201, 434234234234234234):
	if k < 5:
		if divs(x):
			s = max(divs(x)) + min(divs(x))
		else:
			s = 0

		if (s)%123==17:
			print(x, s)
			k += 1

	if k == 5:
		break
