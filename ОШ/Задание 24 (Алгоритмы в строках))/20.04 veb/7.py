s = open("24_7.txt").readline()
s = s.replace("XYZ", "#")
s = s.replace("XY", "*").replace("YZ", "*")

cur = 0
res = 0

for c in s:
	if c == "3":
		cur += 3
	if c == "*":
		cur += 2
	else:
		cur = 0

	res = max(res, cur)

print(res)