a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/2.04 prkt/1.txt")]
sr = sum(x for x in a) / len(a)
res = []

for i in range(len(a) - 1):
	x = a[i:i+2]
	
	if abs(sum(x)) > sr:
		res += [sum(x)]

print(len(res), abs(min(res)))