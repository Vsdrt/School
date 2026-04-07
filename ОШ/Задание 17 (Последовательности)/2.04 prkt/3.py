a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/2.04 prkt/3.txt")]
mn = min(x for x in a if x%17==0)
res = []

for i in range(len(a) - 1):
	x = a[i:i+2]
	if sum(p%mn==0 for p in x)>=1:
		res += [sum(x)]

print(len(res), max(res))