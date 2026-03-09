def divs(x):
	res = set()
	for  i in range(2, int(x**0.5)):
		if x%i==0:
			res.add(i)
			res.add(x//i)

	return sorted(res)

for x in range(700_001, 700_500):

	if len(divs(x)) >=1:
		m = min(divs(x)) + max(divs(x))
	else:
		m = 0
	
	if str(m)[-1]=="8":
		print(x, m)
	

	