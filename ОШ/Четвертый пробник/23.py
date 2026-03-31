def f(st, en):
	if st > en: return 0
	if st == en: return 1
	return f(st + 1, en) + f(st + 3, en)

print(f(1, 8) * f(8, 15))