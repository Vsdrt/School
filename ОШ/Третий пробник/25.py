from functools import lru_cache


@lru_cache(maxsize = None)
def divs(x):
	res = {1, }
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)
	return sorted(res)


k = 0

for n in range(11_000_001, 2356789765432123456789087654321):
	if len(divs(n)) >= 2:
		m = divs(n)[-1] + divs(n)[-2]
	else:
		m = 0

	if k < 5 and 0 < m < 10_000:
		print(m)
		k += 1
	if k == 5:
		break