for a in range(1001):
	for b in range(1001):
		for c in range(1001):
			s = list("0" * a + "1" * b + "3" * c)

			if len(s) == 1000:
				for i in range(len(s)):
					if s[i] == "3":
						s[i] = "0"
					elif s[i] == "0":
						s[i] = "3"	
					
				s = "".join(s)
				sm = sum(map(int, s))

				if sm == 100:
					print(s.count("0"))
					break


