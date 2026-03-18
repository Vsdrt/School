def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i == 0:
			res.add(i)
			res.add(x//i)
	return res


k = 0

for x in range(350001, 351000):
	if len(divs(x)) == 0:
		m = 0
	if len(divs(x)) >= 1:
		m = max(divs(x)) - min(divs(x))

	if m%23 == 9 and k <= 5:
		print(x, m)
		k += 1

	if k == 6:
		break
