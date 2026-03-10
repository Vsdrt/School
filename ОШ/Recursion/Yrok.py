from functools import lru_cache

@lru_cache
def fibb(x):
	global k
	k += 1

	if x < 3:
		return 1
	return fibb(x-1) + fibb(x-2)

k = 0
for x in range(20500):
	fibb(x)
print(fibb(20500))
print(k)