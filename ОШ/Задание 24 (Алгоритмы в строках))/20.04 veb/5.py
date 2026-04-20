s = open("24_5.txt").readline()
s = s.replace("CFE", "*").replace("FCE", "*")

cur = ""
res = 0


for i in s:
	cur += i

	if cur[-1] == "*":
		res = max(res, len(cur))
	else:
		cur = ""

print(res)