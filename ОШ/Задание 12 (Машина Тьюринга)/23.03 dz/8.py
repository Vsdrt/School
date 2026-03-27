s = list("2" * 764 + "3" * 122 + "x" * 114)

for i in range(len(s)):
	if s[i] == "2":
		s[i] = "3"
	
	elif s[i] == "3":
		s[i] = "x"

	elif s[i] == "x":
		s[i] = "2"

s = "".join(s)
cnt = s.count("x")
s = s.replace("x", "0")
sm = sum(map(int, s))

for x in range(10):
	if x * cnt + sm == 3496:
		print(x)