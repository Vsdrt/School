from itertools import product

cif = "0123456789"
res = set()

for k in range(4):
	for a in product(cif, repeat = k):
		a = "".join(a)
		x = f"123{a}890"
		x = int(x)
		if x <= 10**8 and x%27==0:
			res.add(x)

for x in sorted(res):
	print(x, x//27)