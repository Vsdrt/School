from itertools import product


cif = "0123456"
mal = "012"
ch = "0246"

res = set()

for x in product(cif, repeat = 5):
	x = "".join(x) 
	if x[0] != "0" and x[0] in ch and x[-1] not in mal and x.count("4") <= 1:
		res.add(x)

print(len(res))