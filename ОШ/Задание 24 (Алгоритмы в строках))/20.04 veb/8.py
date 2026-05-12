s = open("24_8.txt").readline()

"""
cur = ''
res = 0

for i in s:
	cur += i

	if cur.count("T") == 100:
		res = max(res, len(cur))
	else:
		if cur.count("T") > 100:
			cur = cur[cur.find("T") + 1:]

print(res)
"""

s = s.split("T")
cur = ''
res = 0

for i in range(len(s) - 100):
	res = max(res, sum(map(len, s[i:i+101])))

print(res + 100)