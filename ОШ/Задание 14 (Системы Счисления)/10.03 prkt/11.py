for x in range(0, 2031):
	a = 6**260 + 6**160 + 6**60 - x

	s = ""
	while a > 0:
		s = str(a%6) + s
		a //= 6
	
	if s.count("0") == 202:
		print(x)
		