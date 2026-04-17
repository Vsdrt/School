from itertools import product


s = "ДГИАШЭ"
res = set()

for x in product(s, repeat = 5):
	a = "".join(x)

	if a[0] not in "ИАЭ" and a[-1] not in "ДГШ":
		res.add(a)

print(res, len(res))