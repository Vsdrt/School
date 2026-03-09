def divs(x):
	res = {1, }
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)
	return sorted(res)


def prost(x):
	if x == 1:
		return False
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			return False
	return True


k = 0
for x in range(500_000 - 1, 0, -1):
	pr = [i for i in divs(x) if prost(i)]
	s = sum(pr)
	if s != 0 and s%10==0 and k <= 6:
		k += 1
		print(x, s)


	