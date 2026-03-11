from itertools import product


s = "фокус"
res = set()

for x in product(s, repeat = 5):
	x = ''.join(x)
	res.add(x)

k = 0
for x in sorted(res):
	k +=1 
	if x.count("ф")==0 and x.count("у")==2:
		print(x, k)