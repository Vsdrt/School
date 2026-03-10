for x in range(29):
	a = int("9230874", 29) + x*29**3
	b = int("52406152", 29) + x*29**4
	if (a+b)%28==0:
		print((a+b)//28)