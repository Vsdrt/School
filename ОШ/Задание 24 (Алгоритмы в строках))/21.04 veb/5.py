s = open("24_5.txt").readline()

cur = "DBAC"

while cur + cur[-4] in s:
	cur += cur[-4]

print(len(cur))