s = open("ОШ/Задание 24 (Алгоритмы в строках))/21.04 dz/7 задача/24.txt").readline()
print(s[:50])

combs = []
for x in "QRS":
	for y in "QRS":
		combs += [x + y]
print(combs)

res = 0 
cur = ''

for i in s:
	cur += i

	if cur[-2:] not in combs:
		res = max(res, len(cur))
	else:
		cur = cur[-1:]

print(res)
