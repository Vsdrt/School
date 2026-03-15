a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/15.03 prkt/17_11.txt")]

res = []

for i in range(len(a) - 1):
	x = a[i:i+2]
	if len(str(abs(sum(x)))) == 3 and str(sum(x))[-1] > str(sum(x))[-2]:
		res += [sum(x)]

print(len(res), min(res))