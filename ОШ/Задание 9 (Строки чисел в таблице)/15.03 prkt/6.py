k = 0

for a in open("ОШ/Задание 9 (Строки чисел в таблице)/15.03 prkt/9_06.csv"):
	a = [int(x) for x in a.split(";")]
	a3 = [x for x in a if a.count(x) == 3]
	a1 = [x for x in a if a.count(x) == 1]

	if len(a3) == 3 and len(a1) == 3 and (sum(set(a3)))**2 > (sum(a1))**2:
		k += 1

print(k)