f = open('ОШ/Задание 26 (Сортировка данных)/30.04 dz/5 задача/26.txt')
n = int(f.readline())
a = [int(x) for x in f]
a.sort(reverse=True)

b = []
cnt = 1

for i in range(n):
	if cnt == 6:
		b += [a[i] // 2]
		cnt = 1
	else:
		b += [a[i]]
		cnt += 1

print(sum(b))

