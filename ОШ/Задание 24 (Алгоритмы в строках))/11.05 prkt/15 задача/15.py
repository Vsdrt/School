from re import findall



s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/15 задача/24.txt').readline()
x = '(?:[13579]+)'
find = findall(x, s)
print(find)

res = 0
for i in find:
	i = int(i)

	if i > res:
		res = i
print(res)	
