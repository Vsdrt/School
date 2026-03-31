k = 0

for s in open("ОШ/Четвертый пробник/9.txt"):
	a = sorted(int(x) for x in s.split())

	if ((a[0] * a[1] == a[2] * a[3])\
		or (a[0] * a[3] == a[2] * a[1])\
		or (a[0] * a[2] == a[1] * a[3]))\
		and (a[-2])**2 > a[0] * a[-1]:
		k += 1

print(k)


	
