s = open("ОШ/Задание 24 (Алгоритмы в строках))/20.04 dz/6 задача/24.txt").readline()

combs = []

for x in "BCDF":
	for y in "AEU":
		for z in "BCDF":
			combs += [x + y + z]

print(combs)

for i in combs:
	s = s.replace(i, "*")

cur = ''
res = 0

for i in range(len(s)):
	cur += s[i]

	if cur[-1] == "*":
		res = max(res, len(cur))
	else:
		cur = ''

print(res)