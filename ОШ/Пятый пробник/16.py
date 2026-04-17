from functools import lru_cache


@lru_cache
def f(n):
	if n <= 5:
		return 1
	if n > 5:
		return n + f(n - 2)
	
for n in range(2128):
	f(n)

print(f(2126) - f(2122))