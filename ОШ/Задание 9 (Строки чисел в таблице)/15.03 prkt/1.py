k = 0

for x in open("ОШ/Задание 9 (Строки чисел в таблице)/15.03 prkt/9_01.txt"):
	a = [int(p) for p in x.split()]
	
	c = a[2]
	b = a[1]
	a = a[0]

	D = b**2 - 4 * a * c

	if D > 0:
		k += 1
	

print(k)