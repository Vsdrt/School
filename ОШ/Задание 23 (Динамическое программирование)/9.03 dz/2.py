def f(st, en):
	if st < en: return 0
	if st == en: return 1
	return f(st - 1, en) + f(st // 2, en)

print(f(30, 9) * f(9, 1))