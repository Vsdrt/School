def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i == 0:
			if simple(i) == False:
				res.add(i)
			if simple(x//i) == False:
				res.add(x//i)
	return sorted(res)



def simple(x):
	if x < 2:
		return False
	for i in range(2, int(x**0.5) +1 ):
		if x%i == 0:
			return False
	return True

k = 0

for x in range(912671, 0, -2):
	if len(divs(x)) == 0:
		s = 0
	else:
		s = sum(divs(x))
	
	if k <= 4 and s != 0 and x%s == 0:
		print(x, s)
		k += 1
	if k == 5:
		break 

