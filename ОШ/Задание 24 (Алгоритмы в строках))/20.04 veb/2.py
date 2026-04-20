s = open("24_2.txt").readline()
print(s[:100])

res = 1
cur = ''

for i in s:
	cur += i

	if not all(k in "13579" for k in cur[-3:]):
		res = max(len(cur), res)
	else:
		cur = cur[-2:]

print(res)	