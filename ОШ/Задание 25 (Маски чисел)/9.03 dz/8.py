from itertools import permutations


def simple(x):
	if x == 0 or x == 1:
		return False
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			return False
	return True



def id(x):
	if str(x).count("0") == 0:
		for i in permutations(str(x)):
			i = "".join(i)
			i = int(i)
			if simple(i) and i != x:
				return True
		return False
	return False
		
for x in range(1_411_111_115, 1_411_111_128):
	if id(x):
		print(x)