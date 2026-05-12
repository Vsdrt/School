s = open("24_4.txt").replace()

for c in "6789ABCDEF":
	s = s.replace(c, " ")

for c in "2345":
	s = s.replace(c, "1")

s = s.replace("*", "+")
s = s.replace("++", " ")

while " 00" in s or "+00" in s:
	s = s.replace(" 00", " 0")
	s = s.replace("+00", " 0")

s = s.replace(" 01", " 0")
s = s.replace("+01", " 1")

s = s.replace(" +", " ")
s = s.replace("+ ", " ")

a = [c for c in s.split() if "+" in c]

for c in sorted(a, key = len, reverse=1):
	print(len(c), c)