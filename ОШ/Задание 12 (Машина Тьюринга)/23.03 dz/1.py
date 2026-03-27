s = list(reversed(bin(135)[2:]))

for i in range(len(s)):
	if s[i] == "1":
		s[i] = "0"
	elif s[i] == "0":
		s[i] = "1"

s = "".join(reversed(s))
print(s, int(s, 2))
