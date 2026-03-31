from functools import lru_cache


@lru_cache(maxsize=None)
def divs(x):
	res = set()
	
	for i in range(2 , int(x**0.5) + 1):
		if x%i==0:
			if i != 8 and str(i)[-1] == "8":
				res.add(i)
			if x//i != 8 and str(x//i)[-1] == "8":
				res.add(x//i)
	return sorted(res)


k = 1

for n in range(500_001, 501_000):
	if k <= 5 and divs(n):
		print(n, min(divs(n)))
		k += 1
	if k == 6:
		break
