from itertools import product

s = "балкон"
res = set()

for i in product(s, repeat = 4):
	x = "".join(i)
	if x.count("б") >= 1:
		res.add(x)

print(len(res))