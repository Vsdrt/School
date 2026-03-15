k = 0

for x in open("ОШ/Задание 9 (Строки чисел в таблице)/15.03 prkt/9_05.txt"):
	a = [int(x) for x in x.split()]
	
	if len(set(a)) == 1:
		k += 1
		print(a)

print(k)