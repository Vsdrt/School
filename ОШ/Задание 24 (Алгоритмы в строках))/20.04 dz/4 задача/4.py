s = open("ОШ/Задание 24 (Алгоритмы в строках))/20.04 dz/4 задача/24.txt").readline()
print(s[:50])
combs = []

for x in "AE":
	for y in "BCD":
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
		cur = ""

print(res)