res = 0

for s in open("ОШ/Пятый пробник/9.txt"):
	a = [int(x) for x in s.split()]
	a1 = [x for x in a if a.count(x) == 1]
	a3 =  [x for x in a if a.count(x) == 3]
	
	if len(a3) == 6 and len(a1) == 1 and max(a3) > max(a1):
		res += 1
		print(a)

print(res)