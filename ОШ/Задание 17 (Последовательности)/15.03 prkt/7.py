a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/15.03 prkt/17_07.txt")]

sm = sum(x for x in a if x < 0)
res = []

for i in range(len(a) - 2):
	x = a[i:i+3]
	if max(x) * min(x) > sm:
		res += [sum(x)]

print(len(res), abs(max(res)))