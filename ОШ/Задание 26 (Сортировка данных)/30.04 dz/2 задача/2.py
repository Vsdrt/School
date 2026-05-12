f = open("ОШ/Задание 26 (Сортировка данных)/30.04 dz/2 задача/26.txt")
s, n = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort(reverse=True)

i = 0
b = []

for p in a:
	if sum(b) + a[i] <= s:
		b += [a[i]]
		i += 1
	else:
		i += 1

print(len(b))
print(min(b))