def f(st, en):
	if st < en: return 0
	if st == en: return 1
	return f(st - 3, en) + f(st // 7, en)


print(f(50, 1))