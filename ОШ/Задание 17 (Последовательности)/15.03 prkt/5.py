a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/15.03 prkt/17_05.txt")]

mx = max(x for x in a if str(x)[-1] == "3" and len(str(abs(x)))==3)
res = []

for i in range(len(a) - 2):
	x = a[i:i+3]
	if sum(str(p)[-1] == "3" and len(str(abs(p)))==3 for p in x)>=1 and sum(x)<mx:
		res += [sum(x)]

print(len(res), max(res))