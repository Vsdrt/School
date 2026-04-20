s = open("24_3.txt").readline()
print(s[:50])

cur = ""
res = 1
comb = []

for x in "6789":
	for y in "6789":
		comb += [x + y]

for x in "ABC":
	for y in "ABC":
		comb += [x + y]

print(comb)


for i in s:
	cur += i

	if cur[-2:] not in comb:
		res = max(res, len(cur))
	else:
		cur = i

print(res)