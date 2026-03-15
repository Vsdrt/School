k = 0
for a in open('ОШ/Задание 9 (Строки чисел в таблице)/15.03 prkt/9_07.txt'):
	a = [int(x) for x in a.split()]
	x = a[0]
	y = a[1]
	z = a[2]
	if x < y + z and y < x + z and z < x + y:
		k += 1

print(k)