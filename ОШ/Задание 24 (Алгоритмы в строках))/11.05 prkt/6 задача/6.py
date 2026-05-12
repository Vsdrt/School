s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/6 задача/24.txt').readline()

cur = ''
res = 0

for i in range(len(s)):
	cur += s[i]

	while "PP" in cur:
		cur = cur[1:]

	if 'PP' not in cur:
		res = max(res, len(cur))

print(res)