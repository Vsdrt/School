from itertools import product



cif = "0123456789"
ch = "02468"
bad_pairs = [c + d for c in ch for d in ch]
res = set()

for x in product(cif, repeat = 6):
	x = "".join(x)
	if x[0] != "0" and int(x)%4==0 and len(set(x))==6 and not any(c in x for c in bad_pairs):
		res.add(x)

print(sorted(res), len(res))