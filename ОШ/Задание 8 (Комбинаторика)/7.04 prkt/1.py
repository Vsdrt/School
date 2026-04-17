from itertools import permutations


s = "АССЕМБЛЕР"
res = set()

for a in permutations(s):
	a = "".join(a)
	sm = 0
	k = 0

	for i in a:
		k += 1
		if i in "АЕ":
			sm += k

	if sm == 9:
		res.add(a)

print(len(res))