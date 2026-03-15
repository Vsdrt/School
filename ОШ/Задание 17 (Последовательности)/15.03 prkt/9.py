a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/15.03 prkt/17_09.txt")]

k11 = 0
kr11 = []
k17 = 0
kr17 = []

for i in a:
	if i%11 == 0:
		k11 += 1
		kr11.append(i)

	if i%17 == 0:
		k17 += 1
		kr17.append(i)


if k11 > k17:
	print(k11, min(kr11))
else:
	print(k17, max(kr17))

	