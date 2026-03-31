def f(n):
	if n > 20:
		return n*n*n + n
	if n%2 == 0 and n <= 20:
		return 3 * f(n+1) + f(n+3)
	if n%2 != 0 and n <= 20:
		return f(n+2) + 2 * f(n+3)
	

k = 0

for n in range(1, 1001):
	if str(f(n)).count("1") == 0:
		k += 1

print(k)