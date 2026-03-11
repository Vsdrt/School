from itertools import product


def per(x, n):
	x = "".join(x)
	x = int(x)
	s = ""
	while x > 0:
		s = str(x%n) + s
		x //= n
	return s


cif = "0123456789"
ch_cif= "02468"
res = set()



for x in product(cif, repeat = 7):
	x = per(x, 6)

	if len(x) == 7 and x[0] != "0" and x.count("2") == 1 and "02" not in x and "22" not in x and "42" not in x and\
		"20" not in x and "22" not in x and "24" not in x:
		res.add(x)

print(len(res))

