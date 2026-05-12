s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/8 задача/24.txt').readline()

cur = ''
res = 0

for i in range(len(s)):
	cur += s[i]

	while 'C' in cur or 'F' in cur:
		cur = cur[1:]

	if 'C' not in cur and 'F' not in cur:
		res = max(res, len(cur))
	
print(res)