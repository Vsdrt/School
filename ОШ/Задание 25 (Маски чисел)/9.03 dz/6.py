from itertools import product
from fnmatch import fnmatch



def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			if simple(i) and f(i):
				res.add(i)
			if simple(x//i) and f(x//i):
				res.add(x//i)
	return sorted(res)



def simple(x):
	if x == 0 or x == 1:
		return False
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			return False
	return True


def f(x):
	s = "*3?"
	return fnmatch(str(x), s)
	

cif  = "0123456789"
res = set()
k = 0

for x in range(960_001, 1000000000000):
	if len(divs(x))>=3 and k <= 4:
		print(x, sum(divs(x)))
		k += 1
	if k == 5:
		break