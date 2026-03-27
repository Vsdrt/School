for k in range(29999, 0, -1):

	s = list(reversed(bin(k)[2:]))

	for i in range(len(s)):
		if s[i] == "0":
			s[i] = "1"
		elif s[i] == "1":
			s[i] = "0"
	
	s = int("".join(reversed(s)), 2)

	if s == 77:
		print(k)
	
