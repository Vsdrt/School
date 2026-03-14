def f(st, en):
	if st < en or st == 32: return 0
	if st == en: return 1
	return f(st - 1, en) + f(st - 5, en)


print(f(42, 23) * f(23, 22) * f(22, 9))

