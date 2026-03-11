from itertools import product


s = "skola"
res = set()

for x in product(s, repeat = 3):
	x = ''.join(x)
	if x.count("k") == 1:
		res.add(x)
	
print(len(res))