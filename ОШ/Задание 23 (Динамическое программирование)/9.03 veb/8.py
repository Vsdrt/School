def f(st, en):
	if st > en: return 0
	if st == en: return 1
	res = f(st + 3, en)
	if st ** 2 != st:
		res += f(st ** 2, en)
	if st * 2 != st:
		res += f(st * 2, en)
	return res



res = 0
for st in range(0, 21):
	res += f(st, 20)

print(res)