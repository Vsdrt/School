from itertools import product



def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			if simple(i):
				res.add(i)
			if simple(x//i):
				res.add(x//i)
	return sorted(res)



def simple(x):
	if x == 1 or x == 0:
		return False
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			return False
	return True



cif = "0123456789"
res = set()

for a in cif:
	for k in range(3):
		for b in product(cif, repeat = k):
			b = "".join(b)
			x = f"34{a}8{b}9"
			x = int(x)
			if x <= 10**7 and len(divs(x)) > 4:
				print(x, max(divs(x)))
