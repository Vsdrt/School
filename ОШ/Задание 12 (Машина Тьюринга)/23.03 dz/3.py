for a in range(1001):
	for b in range(1001):
		s = list("0" * a + "1" * a + "2" * b)
		if len(s) == 1000:
			s1 = sum(map(int, s))

			for i in range(len(s)):
				if s[i] == "0":
					s[i] = "1"
				elif s[i] == "1":
					s[i] = "2"
				elif s[i] == "2":
					s[i] = "0"	

			s2 = sum(map(int, s))
			s = "".join(s)

			if s1 == s2 + 200:
				print(s.count("0"))