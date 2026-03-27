for x in range(1001):
	for y in range(1001):
		s = list("0" * x + "1" * x + "2" * y)

		if len(s) == 1000:

			s1 = sum(map(int, s))

			for i in range(len(s)):
				if s[i] == "0":
					s[i] = "2"

				elif s[i] == "1":
					s[i] = "X"
				
				elif s[i] == "2":
					s[i] = "1"

			s = list(reversed(s))

			for i in range(len(s)):
				if s[i] == "0":
					s[i] = "1"

				elif s[i] == "1":
					s[i] = "2"
				
				elif s[i] == "2":
					s[i] = "0"

			s = "".join(s)
			cnt = s.count("X")
			s = s.replace("X", "0")
			s2 = sum(map(int, s))

			if s1 == s2 + 363:
				print(cnt)




