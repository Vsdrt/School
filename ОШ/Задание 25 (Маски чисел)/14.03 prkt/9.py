from math import factorial


def divs(x):
	res = set()
	for i in range(1, int(x**0.5) + 1):
		if x%i == 0:
			if simple(i):
				res.add(i)
			if simple(x//i):
				res.add(x//i)
	return res


def simple(x):
	if x < 2:
		return False
	for i in range(2, int(x**0.5) + 1):
		if x%i == 0:
			return False
	return True

res = set()



for x in range(2, 15):
	if len(divs(factorial(x)))%2 != 0:
		res.add(x)

for x in sorted(res, reverse = True):
	print(x, len(divs(factorial(x))))