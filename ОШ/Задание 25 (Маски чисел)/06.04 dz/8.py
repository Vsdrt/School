def divs(x):
	res= set()
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			res.add(i)
			res.add(x//i)

	return sorted(res)


for x in range(224466, 664423):


	if x%5==0 and x%7==0 and x%13==0 and x%25!=0 and x%49!=0 and x%169!=0 and \
		max(divs(x)) <= 100000 and str(max(divs(x)))[-2:] == "19":
		print(x, max(divs(x)))
		