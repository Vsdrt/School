s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/7 задача/24.txt').readline()

a = {}

for i in range(len(s) - 1):
	pair = s[i:i+2]

	if pair[0] == "X":

		if pair in a:
			a[pair] += 1
		else:
			a[pair] = 1


res = ['', 0]

for pair in a:
	if a[pair] > res[1]:
		res = [pair, a[pair]]

print(res)
