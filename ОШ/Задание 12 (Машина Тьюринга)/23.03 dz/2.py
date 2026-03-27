s = list("x" * 512 + "y" * 200 + "z" * 288)

for i in range(len(s)):
	if s[i] == "x":
		s[i] = "z"
	elif s[i] == "y":
		s[i] = "x"
	elif s[i] == "z":
		s[i] = "x"
		break

s = "".join(s)
print(s.count("x"))