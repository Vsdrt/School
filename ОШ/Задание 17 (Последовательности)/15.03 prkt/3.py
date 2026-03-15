a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/15.03 prkt/17_03.txt")]

mx = max(x for x in a if str(x)[-2:] == "39" and len(str(abs(x))) == 4)
res = []

for i in range(len(a) - 1):
	x = a[i:i+2]
	if sum(len(str(abs(p))) == 4 for p in x)==1 and (sum(x))**2 <= mx**2:
		res += [sum(x)]

print(len(res), max(res))