def f(st, en):
	if st < en: return 0
	if st == en: return 1
	return f(st - 8, en) + f(st // 2, en)


print(f(102, 43) * f(43, 5))