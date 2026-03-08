from itertools import permutations

s = "prosto"
res = set()

for x in permutations(s):
	a = "".join(x)
	if "pp" not in a and "rr" not in a and "oo" not in a and\
	"ss" not in a and "tt" not in a:
		res.add(a)

print(len(res))