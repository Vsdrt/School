from itertools import product


cif = "01234567"
res = set()

for x in product(cif, repeat =5):
	x = ''.join(x)
	if x[0] != "0" and x.count("6")==1 and "16" not in x and "36" not in x and "56" not in x and "76" not in x  and\
	"61" not in x and "63" not in x and "65" not in x and "67" not in x  :
		res.add(x)

print(res, len(res))