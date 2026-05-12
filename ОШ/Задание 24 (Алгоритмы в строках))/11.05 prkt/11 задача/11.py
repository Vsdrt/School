s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/11 задача/24.txt').readline()

cnt = 0

for i in range(len(s) - 4):
	x = s[i:i+5]

	if x == x[::-1]:
		cnt += 1

print(cnt)