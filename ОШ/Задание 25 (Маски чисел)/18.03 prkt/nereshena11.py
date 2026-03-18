from functools import lru_cache
from itertools import product


@lru_cache
def simple(x):
	if x < 2:
		return False
	if x == 2:
		return True
	if x%2==0:
		return False
	for i in range(3, int(x**0.5) + 1, 2):
		if x%i==0:
			return False
	return True

@lru_cache
def divs(x):
	res = set()
	for i in range(1, int(x**0.5) + 1):
		if x%i==0:
			if simple(i):
				res.add(i)
			if simple(x//i):
				res.add(x//i)
	return sorted(res)
			


@lru_cache(maxsize = None)
def solve(x):
	q = set([x for x in range(301) if simple(x)])
	res = []

	for i in q:
		if len(res) == 4:
			return res
		if x%i==0:
			res += [i]
			x = x // i

	return []

cif = "0123456789"
mn = 10**11
mx = 0

for k in range(9):
	for p in range(9 - k):
		for a in product(cif, repeat = k):
			for b in product(cif, repeat = p):
				a = "".join(a)
				b = "".join(b)
				x = f"{a}5{b}3"
				x = int(x)
				if x <= 10**10 and len(solve(x)) == 4:
					if x < mn:
						mn = x
					if x > mx:
						mx = x
					

m = min(divs(mn)) * max(divs(mn))
n = divs(mx)[1] * divs(mx)[2]

print(m*n)

