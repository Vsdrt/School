def solve(n):
	a = bin(n)[2:]
	a = "1"*a.count("1")
	return int(a, 2)

res = set()
for n in range(10, 2501):
	res.add(solve(n))

print(len(res))



