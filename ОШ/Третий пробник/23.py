def f(st, en):
	if st > en or st == 6:
		return 0
	if st == en:
		return 1
	return f(st + 2, en) + f(st * 3, en)

print(f(1, 25) * f(25, 63))