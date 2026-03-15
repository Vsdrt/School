a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/15.03 prkt/17_04.txt")]

mn = min(p for p in a)
res = []

for i in range(len(a) - 1):
	x = a[i:i+2]
	if sum(p%117==mn for p in x)>=1:
		res += [sum(x)]

print(len(res), max(res))