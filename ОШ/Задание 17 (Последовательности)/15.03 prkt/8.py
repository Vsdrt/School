a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/15.03 prkt/17_08.txt")]


sm = sum(x for x in a if x%2==0 and len(str(abs(x)))==2)
res = []


for i in range(len(a) - 1):
	x = a[i:i+2]
	if sum(p%sm==0 for p in x)==1:
		res += [x[0] * x[1]]


print(len(res), abs(min(res)))