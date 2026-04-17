from functools import lru_cache


@lru_cache
def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i == 0:
			if i != 7 and str(i)[-1] == "7":
				res.add(i)
			if x//i != 7 and str(x//i)[-1] == "7":
				res.add(x//i)

	return sorted(res)


k = 1

for n in range(1_125_001, 1_126_000):
	if len(divs(n)) > 0 and k <= 5:
		print(n, min(divs(n)))
		k += 1