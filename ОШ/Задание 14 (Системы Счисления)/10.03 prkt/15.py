for x in range(19):
	
	a = int("01418", 13) + x*13**4
	b = int("10037", 14) + x*14**3
	c = int("20209", 19) + x*19**3
	if a + b == c:
		print(x, c)
