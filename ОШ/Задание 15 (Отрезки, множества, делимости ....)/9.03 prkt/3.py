def f(x, a):
	p = 10 <= x <= 45
	q = 35 <= x <= 78
	return ((not p) <= (q)) and (not a)


mn = 10**10
for st in range(0, 200):
	for en in range(st, 200):
		if all(not f(x//4, st <= x//4 <= en) for x in range(-800, 800)):
			if en - st < mn:
				mn = en - st

print(mn)