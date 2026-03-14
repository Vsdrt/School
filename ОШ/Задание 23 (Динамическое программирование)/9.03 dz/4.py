def f(st, en):
	if st > en or st == 22: return 0
	if st == en: return 1
	return f(st + 1, en) + f(st + 3, en) + f(st ** 2, en)



print(f(2, 17) * f(17, 25))