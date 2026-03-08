x = 3*1024**75 + 2*256**76 - 16**77 - 2023
s = ""

while x > 0:
	s = str(x%32) + s
	x //= 32

print(s.count("0"), s)
