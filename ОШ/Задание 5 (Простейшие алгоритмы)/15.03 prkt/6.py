def f(n):
	cif = sorted([x for x in str(n)])
	mn = ""
	for i in cif:
		if i != "0":
			mn += i

	cif = sorted([x for x in str(n)], reverse=True)
	mx = ""
	for i in cif:
		mx += i

	return int(mn[:2]), int(mx[:2])
	
def solve(n):
	a = f(n)
	return max(a) - min(a)

k = 0

for n in range(100, 1000):
	print(n, f(n), solve(n))
	if solve(n) == 58:
		k += 1

print(k)

