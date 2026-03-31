for x in "0123456789abcdefgh":
	a = int("10253", 18) + int(x, 18) * 18**3
	b = int("3208", 18) + int(x, 18) * 18**1
	if (a + b)%7==0:
		print((a + b)//7)