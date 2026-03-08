from itertools import product

def kv(x):
	for i in range(0, 100000+1):
		if x == i**2:
			return True
	else:
		return False


cif = "0123456789"
res = set()
for a in cif:
	for k in range(8):
		for b in product(cif, repeat = k):
			b = "".join(b)
			x = "1" + a + "2" + b + "4"
			x = int(x)
			if x <= 10**10 and x%2024==0 and kv(x) == True:
				res.add(x)

for x in sorted(res):
	print(x, x//2024)