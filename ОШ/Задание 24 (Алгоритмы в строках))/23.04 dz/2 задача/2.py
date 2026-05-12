s = open("ОШ/Задание 24 (Алгоритмы в строках))/23.04 dz/2 задача/24.txt").readline().rstrip()

s = s.replace("*", "+")

while "++" in s or "+0" in s:
	s = s.replace("++", "+ +")
	s = s.replace("+0", " +")

mx = 0

for i in sorted(s.split(), key = len, reverse=1)[:5]:
	i = i.split("+")
	
	mx = max(len(i), mx)

print(mx)