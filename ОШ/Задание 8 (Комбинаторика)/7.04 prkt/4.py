from itertools import product


s = "ЛАЙМ"
res = set()

for a in product(s, repeat = 5):
	a = "".join(a)
	res.add(a)

k = 0

for i in sorted(res):
	k += 1
	if i.count("М") == 0 and i.count("Л") == 0 and "ЙЙ" not in i:
		print(i, k)