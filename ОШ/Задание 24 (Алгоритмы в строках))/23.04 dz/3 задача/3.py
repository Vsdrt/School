s = open("ОШ/Задание 24 (Алгоритмы в строках))/23.04 dz/3 задача/24.txt").readline()

for i in "BCD":
	s = s.replace(i," ")

while "AA" in s:
	s = s.replace("AA", " A") 
	
s = s.replace("A+", "A ")
s = s.replace("*", " ")
s = s.replace("-", " ")
s = s.replace("++", "+ +")
s = s.replace("+ ", " ")

a = [c for c in s.split() if c[0] == "A" and c.count("A") == 1 and len(c)>1]

mx = 0

for i in sorted(a, key=len, reverse=1):
	i = i[1:]
	res = eval(i)
	mx = max(res, mx)

print(mx)
