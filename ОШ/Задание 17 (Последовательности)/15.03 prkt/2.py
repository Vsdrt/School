a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/15.03 prkt/17_02.txt")]

k = sum(x%100==0 for x in a)
res = []


for i in range(len(a) - 1):
	x = a[i:i+2]
	if sum(p<0 for p in x)>=1 and sum(x) < k:
		res += [sum(x)]

print(len(res), abs(max(res)))