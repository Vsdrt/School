from itertools import product



def divs(x):
	res = set()
	for i in range(1, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)
	return sorted(res)


st = [2**x for x in range(1, 50)]
cif = "0123456789"
res = set()

for c in cif:
	for k in range(5):
		for p in range(5 - k):
			for a in product(cif, repeat = k):
				for b in product(cif, repeat = p):
					a = "".join(a)
					b = "".join(b)
					x = f"{a}31{b}65{c}"
					x = int(x)
					if x <= 10**9 and x%31==0 and\
						  x%2031==0 and len(divs(x)) in st:
						res.add(x)

for x in sorted(res):
	print(x, x//2031)
