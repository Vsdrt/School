from itertools import product


cif = "0123456789abcde"
res = set()

for x in product(cif, repeat = 5):
	x = ''.join(x)
	if x[0] != "0" and x.count("8")==1 and sum(int(c, 15)>9 for c in x)>=2:
		res.add(x)

print(len(res))