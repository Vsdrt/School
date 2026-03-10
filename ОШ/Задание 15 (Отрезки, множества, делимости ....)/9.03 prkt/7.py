def f(x, a):
	p = 40 <= x <= 45
	q = 10 <= x <= 33
	return ((q) and not(a)) <= (p)

mn = 10**10
for st in range(0, 100):
	for en in range(st, 100):
		if all(f(x//4, st <= x//4 <= en) for x in range(-1000, 1000)):
			if en - st < mn:
				mn = en - st

print(mn)
			