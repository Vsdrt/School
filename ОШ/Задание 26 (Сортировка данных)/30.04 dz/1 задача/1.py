f = open('ОШ/Задание 26 (Сортировка данных)/30.04 dz/1 задача/26.txt')
s, n = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort()
b = []
i = 0
while sum(b) + a[i] <= s:
	b += [a[i]]
	i += 1
print(len(b))

while sum(b) + a[i] - b[-1] <= s:
	b[-1] = a[i]
	i += 1

print(b[-1])