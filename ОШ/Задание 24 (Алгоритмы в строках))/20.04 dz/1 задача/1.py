s = open("ОШ/Задание 24 (Алгоритмы в строках))/20.04 dz/1 задача/24.txt").readline()

combs = []

for x in "CDF":
	for y in "AU":
		combs += [x + y]

print(combs)

for i in combs:
	s = s.replace(i, "*") 

cur = ""
res = 0

for i in s:
	cur += i

	if i == "*":
		res = max(res, len(cur))
	else:
		cur = ''

print(res)
