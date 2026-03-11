from itertools import product


cif = "0123456"

bad_pairs = [c + d for c in cif for d in cif if c == d]
res = set()

for x in product(cif, repeat= 5):
	x = "".join(x)
	if x[0] != "0" and x.count("6") == 1 and not any(c in x for c in bad_pairs):
		res.add(x)
	
print(sorted(res), len(res))