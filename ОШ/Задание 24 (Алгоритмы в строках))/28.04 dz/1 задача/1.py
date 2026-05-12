s = open("ОШ/Задание 24 (Алгоритмы в строках))/28.04 dz/1 задача/24.txt").readline()

cur = ''
res = 0

for i in s:
	cur += i

	if "XIX" not in cur:
		res = max(res, len(cur))
	else:
		cur = cur[1:]

print(res)