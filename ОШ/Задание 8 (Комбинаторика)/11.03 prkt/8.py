from itertools import product

nch= "1357"
cif = "012345678"
qw = '18'
res = set()

for x in product(cif, repeat = 5):
	x = ''.join(x)
	if len(x)==5 and x[0] != "0" and x[0] not in nch and x[-1] not in qw and x.count("3") <= 1:
		res.add(x)

print(len(res))