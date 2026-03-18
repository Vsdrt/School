from functools import lru_cache
from time import time

@lru_cache
def simple(x):
	if x < 2:
		return False
	if x == 2:
		return True
	if x%2 == 0:
		return False
	for i in range(3, int(x**0.5) + 1, 2):
		if x%i==0:
			return False
	return True

@lru_cache
def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i==0 and simple(i) == False:
			res.add(i) 
		if x%i==0 and simple(x//i) == False:
			res.add(x//i)
	return res

start = time()

k = 0

for x in range(987_652, 0, -1):
	if divs(x):
		r = sum(divs(x))
	else:
		r = 0
	
	if str(r)[-1] == "7" and k < 5:
		print(x)
		k += 1

	if k == 5:
		break 

print(time()-start)