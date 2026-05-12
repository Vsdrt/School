s = open("ОШ/Задание 24 (Алгоритмы в строках))/20.04 dz/3 задача/24.txt").readline()

combs = []

for x in "ABC":
	for y in "ABC":
		combs += [x + y]

for x in "89":
	for y in "89":
		combs += [x + y]

print(combs)

cur = ''
res = 0

for i in s:
	cur += i

	if cur[-2:] not in combs:
		res = max(res, len(cur))
	else:
		cur = i

print(res)