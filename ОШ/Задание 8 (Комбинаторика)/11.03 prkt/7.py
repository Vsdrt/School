from itertools import product


s = "лемур"
res = set()

for x in product(s, repeat = 4):
	x = ''.join(x)
	res.add(x)


k = 0

for x in sorted(res):
	k += 1
	if x[0] == "л":
		print(k)
		break