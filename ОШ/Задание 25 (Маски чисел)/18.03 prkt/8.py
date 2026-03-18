import time
from functools import lru_cache

@lru_cache(maxsize= None)
def divs(x):
	res = set()
	for i in range(1, int(x**0.5) + 1):
		if x%i == 0:
			res.add(i)
			res.add(x//i)
	return sorted(res)

start = time.time()

for x in range(164_701, 164_753):
	if len(divs(x)) == 6:
		print(divs(x)[-2], divs(x)[-1])

print(time.time() - start)