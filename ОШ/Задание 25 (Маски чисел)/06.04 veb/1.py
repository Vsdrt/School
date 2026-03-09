def divs(x):
	res = set()
	for i in range(1, int(x**0.5)+1):
		if x%i==0:
			res.add(i)
			res.add(x//i)
	return sorted(res)


for x in range(126849, 126871+1):
	if len(divs(x))==4:
		print(divs(x)[-2:])