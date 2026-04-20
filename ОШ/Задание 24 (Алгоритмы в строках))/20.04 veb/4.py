s = open("24_4.txt").readline()
# s = "__X--X##Y**Y" # проверка на простом примере 

cur = ''
res = 0

for i in s:
	if cur.count("X") == 1 and cur.count("Y") == 1:
		res = max(res, len(cur))
	else:
		if cur.count("X") > 1:
			cur = cur[cur.find("X") + 1:]
		if cur.count("Y") > 1:
			cur = cur[cur.find("Y") + 1:]
	# print(cur, res)

print(res)