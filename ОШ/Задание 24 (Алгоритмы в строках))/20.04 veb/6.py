s = open("24_6.txt").readline()

comb = []

for x in "24":
	for y in "135":
		comb += [x + y]

print(comb)

for i in comb:
	s = s.replace(i, "*")

cur = ""
res = 0

for i in s:
	cur += i

	if i == "*":
		res = max(res, len(cur))
	else:
		cur = ""

print(res)