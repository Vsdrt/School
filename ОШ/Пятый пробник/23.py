def f(st, en):
	if st > en or st == 35:
		return 0
	if st == en:
		return 1
	return f(st + 1, en) + f(st + 2, en) + f(st * 2, en)


print(f(7, 13) * f(13, 15) * f(15, 51))