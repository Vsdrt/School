def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)
	return sorted(res)


def prost(x):
	if x == 1 or x == 0:
		return False
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			return False
	return True



k = 1
for x in range(1_273_548, 2000000000):
	sm = sum(divs(x))
	if prost(sm%100_000) and k <= 5:
		print(x, sm)
		k += 1
	if k == 6:
		break

