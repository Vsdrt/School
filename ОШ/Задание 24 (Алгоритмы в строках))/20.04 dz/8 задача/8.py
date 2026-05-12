s = open("ОШ/Задание 24 (Алгоритмы в строках))/20.04 dz/8 задача/24.txt").readline()
print(len(s))

res = 0
cur = ""

for i in range(len(s)):
	cur += s[i]

	while cur.count("AB") > 50:
		cur = cur[1:]

	if cur.count("AB") == 50:
		res = max(res, len(cur))

print(res)