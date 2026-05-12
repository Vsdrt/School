from re import *



s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/9 задача/24.txt').readline()
x = '(?:0|[1-9][0-9]*)'
a = findall(x, s)

nch = []

for i in a:
	x = int(i)
	if x%2 != 0:
		nch += [x]

print(min(nch))