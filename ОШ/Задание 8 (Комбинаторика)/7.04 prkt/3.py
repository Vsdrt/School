from itertools import product


s = "ПАРУС"
res = set()

for a in product(s, repeat = 5):
	a = "".join(a)

	res.add(a)

k = 0

for i in sorted(res):
	k += 1

	if i[0] == "У" and "АА" not in i:
		print(i, k)
		break