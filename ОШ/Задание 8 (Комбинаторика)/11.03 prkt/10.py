from itertools import product


cif = "01234567"
ch = "0246"
nch = "1357"
bad_pairs = [c + d for c in ch for d in ch] + [c + d for c in nch for d in nch]
res = set()

for x in product(cif, repeat = 5):
	x = ''.join(x)
	if x[0] != "0" and x.count("1")==0 and len(set(x))==5 and not any(c in x for c in bad_pairs):
		res.add(x)

print(len(res))