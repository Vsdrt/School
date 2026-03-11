from itertools import product


cif = "0123456789"
res = set()

for x in product(cif, repeat = 5):
	x = "".join(x)
	if x[0] != "0":
		res.add(x)


k = 0
ch = "02468"
nch = "13579"
bad_pairs = [c + d for c in ch for d in ch] + [c + d for c in nch for d in nch]

for x in sorted(res):
	k += 1
	if not any(c in x for c in bad_pairs) and k%15==0:
		print(k, x)
