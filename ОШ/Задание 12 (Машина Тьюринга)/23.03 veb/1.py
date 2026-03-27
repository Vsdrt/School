for x in range(1001):
	for y in range(1001):

		s = list(x * "0" + y * "1" + y * "2")

		if len(s) == 1000:		
			s1 = sum(map(int, s))

			for i in range(len(s)):
				if s[i] == "0":
					s[i] = "2"
				elif s[i] == "1":
					s[i] = "0"
				elif s[i] == "2":
					s[i] = "1"

			s2 = sum(map(int, s))
			
			if s1 == s2 + 178:
				print(y)