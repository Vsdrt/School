a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/2.04 prkt/5.txt")]
mn = min(x for x in a if x > 0 and x%19==0)
res = []

for i in range(len(a) - 1):
	x = a[i:i+2]

	if sum(x) < mn:
		res += [sum(x)]

print(len(res), abs(max(res)))