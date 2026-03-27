s = list((reversed("1" * 400 + "2" * 250 + "3" * 350)))

for i in range(len(s)):
	if s[i] == "1":
		s[i] = "3"
	elif s[i] == "2":
		s[i] = "3"
	elif s[i] == "3":
		s[i] = "2"

q = "".join(s)
print(q.count("3"))