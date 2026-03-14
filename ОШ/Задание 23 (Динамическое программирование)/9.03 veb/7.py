def f(st, en):
	if st > en: return 0
	if st == en: return 1
	return f(st + 1, en) + f(st * 2, en) + f(st * 3, en)
	

sm = 0
for x in (2, 4, 6, 8, 10, 12, 14):
	sm += f(x, 15)

print(sm)
