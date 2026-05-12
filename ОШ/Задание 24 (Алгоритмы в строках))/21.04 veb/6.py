s = open("24_6.txt").readline()

cur = "KLMN" * 2

for k in range(len(cur)):
	cur = cur[k:]

	while cur + cur[-4] in s:
		cur += cur[-4]

	print(len(cur))