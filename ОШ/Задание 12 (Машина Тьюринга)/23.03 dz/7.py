s = list(reversed("0" * 1000 + "1" * 500))
q = 1

for i in range(len(s)):
	if s[i] == "0" and q == 1:
		s[i] = "1"
		q = 2

	elif s[i] == "0" and q == 2:
		s[i] = "0"
		q = 3

	elif s[i] == "0" and q == 3:
		s[i] = "0"
		q = 4

	elif s[i] == "0" and q == 4:
		s[i] = "0"
		q = 1
	
	elif s[i] == "1" and q == 1:
		s[i] = "0"
		q = 3
	
	elif s[i] == "1" and q == 2:
		s[i] = "1"
		q = 3
	
	elif s[i] == "1" and q == 3:
		s[i] = "1"
		q = 4
	
	elif s[i] == "1" and q == 4:
		s[i] = "1"
		q = 1

s = "".join(reversed(s))
print(sum(map(int, s)))