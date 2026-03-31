for x in range(1000000): 
	t = 27 * 60 + 27
	i = 2 * 56000 * t * 15
	i += 28 * x * 2 ** 13
	s = 367_217_732

	if i / s > 332:
		print(x)
		break