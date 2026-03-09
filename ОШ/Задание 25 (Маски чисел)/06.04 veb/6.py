def simple(x):
	if x == 1:
		return False
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			return False
	
	return True


for x in range(125_697, 125_721 + 1):
	for a in range(1, int(x**0.5) + 1):
		if x%a==0 and simple(a) and simple(x//a):
			print(a, x//a)