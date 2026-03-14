def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i == 0:
			res.add(i)
			res.add(x//i)
	return res


k = 0

for x in range(452_022, 500_000):
	if len(divs(x)) == 0:
		m = 0
	else:
		m = min(divs(x)) + max(divs(x))
	
	if m % 7 == 3 and k <= 4:
		print(x, m)
		k += 1
	if k == 5: break 
