s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/14 задача/24.txt').readline()

a = {}

for i in range(len(s) - 1):
	pair = s[i:i+2]

	if pair[0] == 'A':

		if pair in a:
			a[pair] += 1
		else:
			a[pair] = 1

print(a)

res = ['', 0]

for i in sorted(a):
	if a[i] > res[1]:
		res[1] = a[i]
		res[0] = i[1:]

print(res)

