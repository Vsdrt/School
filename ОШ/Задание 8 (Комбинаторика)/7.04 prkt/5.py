from itertools import product


cif = "0123456789ABCDEF"
res = set()

for a in product(cif, repeat = 4):
	a = "".join(a)

	if a.count("3") == 1\
		and a[0] != "0"\
		and "00" not in a\
		and "11" not in a\
		and "22" not in a\
		and "33" not in a\
		and "44" not in a\
		and "55" not in a\
		and "66" not in a\
		and "77" not in a\
		and "88" not in a\
		and "99" not in a\
		and "AA" not in a\
		and "BB" not in a\
		and "CC" not in a\
		and "DD" not in a\
		and "EE" not in a\
		and "FF" not in a:
		res.add(a)

print(len(res))