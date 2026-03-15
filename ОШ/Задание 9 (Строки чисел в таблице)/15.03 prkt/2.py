k = 0

for q in open("ОШ/Задание 9 (Строки чисел в таблице)/15.03 prkt/9_02.txt"):
	x = sorted([int(x) for x in q.split()])

	if (90) in x:
		x.remove(90)
		if sum(x) == 90:
			k += 1


print(k)


