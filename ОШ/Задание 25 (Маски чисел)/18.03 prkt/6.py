import time
from functools import lru_cache

@lru_cache(maxsize = None)
def divs(x):
	res = set()
	for i in range(2, int(x**0.5) + 1):
		if x%i == 0:
			res.add(x//i)
			res.add(i)
	return res 

start = time.time()

k = 0

for x in range(700_001, 382934704723040934):
	if divs(x):
		m = max(divs(x)) + min(divs(x))
	else:
		m = 0

	if str(m)[-1] == "8" and k < 5:
		print(x, m)
		k += 1
	
	if k == 5:
		break


print(time.time() - start)