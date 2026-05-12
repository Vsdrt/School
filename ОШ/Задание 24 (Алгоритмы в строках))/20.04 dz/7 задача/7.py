s = open("ОШ/Задание 24 (Алгоритмы в строках))/20.04 dz/7 задача/24.txt").readline()

combs = ["AB", "CAC"]


s = s.replace("AB", "*").replace("CAC", "#")

cur = ''
res = 0

for i in range(len(s)):
	cur += s[i]

	if cur[-1] == "*" or cur[-1] == "#":
		cur = cur.replace("*", "AB").replace("#", "CAC")
		res = max(res, len(cur))
	else:
		cur = ''

print(res)