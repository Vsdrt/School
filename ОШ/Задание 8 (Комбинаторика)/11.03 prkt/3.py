from itertools import product

s = "парус"
res = set()

for x in product(s, repeat = 5):
	x = ''.join(x)
	res.add(x)

k = 0
for x in sorted(res):
	k += 1
	if x.count("у") <= 1 and "аа" not in x:
		print(x, k)
		break 