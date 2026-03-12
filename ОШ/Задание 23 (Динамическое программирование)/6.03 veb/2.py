from functools import lru_cache

@lru_cache
def f(n):
	if n < 1:
		return 0
	elif n == 1:
		return 1
	elif n % 2 == 0: 
		return f(n - 1) + f(n - 3) + f(n // 2)
	return 	f(n - 1) + f(n - 3)


for x in range(15):
	f(x)

print(f(15))