a = [int(x) for x in open("ОШ/Четвертый пробник/17.txt")]
mx = max(p for p in a if len(str(abs(p)))> 1 and str(p)[-2:] == "17")
res = []

for i in range(len(a) - 2):
	x = a[i:i+3]
	if sum(len(str(abs(p)))==4 for p in x)==2\
		and sum(p%5==0 for p in x)>=1\
		and sum(x) > mx:
		res += [sum(x)]

print(len(res), max(res))
