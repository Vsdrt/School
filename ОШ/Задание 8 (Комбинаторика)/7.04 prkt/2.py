from itertools import product


s = "ГЕПАРД"
res = set()

for a in product(s, repeat = 5):
	a = "".join(a)

	if a.count("Г") == 1 and a[0] != "А" and a[-1] != "Е":
		res.add(a)

print(len(res))