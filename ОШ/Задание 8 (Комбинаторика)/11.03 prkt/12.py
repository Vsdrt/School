from itertools import product



cif = "0123456789abcdef"
ch = "02468ace"
nch = "13579bdf"
bad_pairs = [c + d for c in ch for d in ch] + [c + d for c in nch for d in nch]
res = set()

for x in product(cif, repeat = 3):
	x = "".join(x)
	if x[0] != "0" and len(set(x)) == 3 and not any(c in x for c in bad_pairs):
		res.add(x)

print(len(res))