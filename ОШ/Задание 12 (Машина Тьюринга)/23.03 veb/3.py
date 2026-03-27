s = list(reversed(bin(992)[2:]))
q = 1

for i in range(len(s)):
	
	if s[i] == "1" and q == 1:
		s[i] = "0"
		q = 2	

	elif s[i] == "0" and q == 1:
		s[i] = "1"
		q = 2

	elif s[i] == "1" and q == 2:
		s[i] = "1"
		q = 3	
	
	elif s[i] == "0" and q == 2:
		s[i] = "1"
		q = 2

	elif s[i] == "0" and q == 3:
		s[i] = "0"
		q = 3
	
	elif s[i] == "1" and q == 3:
		s[i] = "0"
		q = 2

	

s = "".join(reversed(s))
print(s, int(s, 2))
