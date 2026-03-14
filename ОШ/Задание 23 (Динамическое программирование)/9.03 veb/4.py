def f(st, en):
	if st < en or st == 35: return 0
	if st == en: return  1
	return f(st // 3, en) + f(st - 2, en) + f(st - 5, en)

print(f(41, 37) * f(37, 8))