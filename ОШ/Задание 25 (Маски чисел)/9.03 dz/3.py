from itertools import product



def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)
	return sorted(res)



cif = "0123456789"
res = set()

for a in cif:
	for k in range(4):
		for b in product(cif, repeat = k):
			b = "".join(b)
			x = f"12{a}{b}45"
			x = int(x)
			if x <= 10**7 and len(divs(x)) == 18:
				res.add(x)

for x in sorted(res):
	print(x, max(divs(x)))