from itertools import product

gl = "ia"
s = "visna"
res = set()

for x in product(s, repeat = 6):
	x = ''.join(x)
	if x.count("v") <= 1 and x[0] != "s" and x[-1] not in gl:
		res.add(x)

print(len(res))

