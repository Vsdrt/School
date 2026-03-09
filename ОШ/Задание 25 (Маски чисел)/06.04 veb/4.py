def divs(x):
	res = set()
	for i in range(2, int(x**0.5)+1):
		if x%i==0:
			res.add(i)
			res.add(x//i)

	return sorted(res)

for x in range(1_204_300, 1_204_380+1):
	nt = set()

	for i in divs(x):
		if i > 0 and i%2==0:
			nt.add(i)

	s = sum(nt)

	if s > 0 and s%10 == 0:
		print(x, s) 
