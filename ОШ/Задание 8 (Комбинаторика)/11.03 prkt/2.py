from itertools import product


cif = "0123456789ab"
res = set()

for x in product(cif, repeat = 5):
	x = "".join(x)
	if len(x) == 5 and x[0] != "0" and x.count("7") == 1 and sum(int(c, 12) > 8 for c in x)<=3:
		res.add(x)

print(len(res))