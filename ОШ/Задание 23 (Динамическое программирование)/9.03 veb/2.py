def f(st, en):
	if st == en: return 1
	if st < en or st == 9 or st == 16: return 0
	return f(st - 1, en) + f(st - 2, en) + f(st // 3, en)

print(f(19, 3))





