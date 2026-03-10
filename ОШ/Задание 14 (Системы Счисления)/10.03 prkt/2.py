for x in range(33):
	a = int("12034", 33) + x*33**2 
	b = int("4909", 33)  + x*33**1
	if (a+b)%19 == 0:
		print(x, (a+b)//19)