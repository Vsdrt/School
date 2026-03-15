k =  0

for x in open("ОШ/Задание 9 (Строки чисел в таблице)/15.03 prkt/9_04.txt"):
	a = sorted([int(p) for p in x.split()])
	
	if (a[-1])**2 > a[0] * a[1] * a[2] * a[3]:
		k += 1
	
print(k)