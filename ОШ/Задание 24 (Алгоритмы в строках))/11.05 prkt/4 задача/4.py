s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/4 задача/24.txt').readline()

cur = ''
res = 0

for i in range(len(s)):
	cur += s[i]

	while "ad" in cur or 'da' in cur:
		cur = cur[1:]

	if 'ad' not in cur and 'da' not in cur:
		res = max(res, len(cur))

print(res)
		