for x in range(19):
	a = int("98897021", 19) + x*19**2
	b = int("20923", 19) + x*19**3
	if (a+b)%18==0:
		print((a+b)//18)