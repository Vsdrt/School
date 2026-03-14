def f(st, en):
	if st > en: return 0
	if st == en: return 1
	return f(st + 1, en) + f(st * 2, en) + f(st * 2 + 1, en) + f(st * 10, en)


print(f(1, 15))