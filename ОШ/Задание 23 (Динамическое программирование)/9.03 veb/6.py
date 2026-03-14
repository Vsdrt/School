def f(st, en, ban = []):
	if st > en or st in ban: return 0
	# if st == 21: return 0   для a
	# if st == 15: return 0   для b
	if st == en: return 1
	return f(st + 1, en, ban) + f(st + 2, en, ban) + f(st * 3, en, ban)

print(f(6, 15) * f(15, 25, [21]) + f(6, 21, [15]) * f(21, 25))

a = f(6, 15) * f(15, 25)
b = f(6, 21) * f(21, 25)