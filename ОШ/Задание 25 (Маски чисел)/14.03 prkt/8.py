def divs(x):
	res = set()
	for i in range(2, int(x ** 0.5) + 1):
		if x%i == 0:
			if simple(i):
				res.add(i)
			if simple(x//i):
				res.add(x//i)
	return res


def simple(x):
	if x == 0 or x == 1:
		return False
	for i in range(2, int(x ** 0.5) + 1):
		if x%i == 0:
			return False
	return True


k = 0

for x in range(22_801, 25_000):
	if len(divs(x)) == 0:
		e = 0
	else:
		e = max(divs(x)) - min(divs(x))

	if e % 47 == 17 and k <= 4:
		print(x, e)
		k += 1
	if k == 5:
		break
	