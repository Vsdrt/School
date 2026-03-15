a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/15.03 prkt/17_10.txt")]

res = []

for i in a:
	if i % 13 == 4 and i % 8 == 1:
		res += [i]

print(max(res), sum(res))