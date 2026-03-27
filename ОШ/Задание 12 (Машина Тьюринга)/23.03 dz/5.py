s = list("0" * 45 + "1" * 21)

q = 1

for i in range(len(s)):
	if s[i] == "1" and q == 1:
		s[i] = "0"
		q = 3

	elif s[i] == "1" and q == 2:
		s[i] = "0"
		q = 1	
	
	elif s[i] == "1" and q == 3:
		s[i] = "1"
		q = 2

	elif s[i] == "0" and q == 1:
		s[i] = "1"
		q = 2
	
	elif s[i] == "0" and q == 2:
		s[i] = "0"
		q = 3
	
	elif s[i] == "0" and q == 3:
		s[i] = "1"
		q = 1

q = "".join(s)

print(q.count("0"))