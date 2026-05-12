s = open("ОШ/Задание 24 (Алгоритмы в строках))/20.04 dz/2 задача/24.txt").readline()
s = s.replace("BA", "*").replace("DA", "*")

cur = ''
res = 0

for i in s:
	cur += i

	if i == "*":
		res = max(res, len(cur))
	else:
		cur = ""

print(res)