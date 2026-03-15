k = 0 

for a in open("ОШ/Задание 9 (Строки чисел в таблице)/15.03 prkt/9_03.txt"):
	a = [int(x) for x in a.split()]
	a2 = [x for x in a if a.count(x) == 2]
	a1 = [x for x in a if a.count(x) == 1]

	if len(set(a2)) >= 1 and all(x > y for x in a2 for y in a1):
		k += 1

print(k)