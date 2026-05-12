s = open("24_5.txt").readline()

s = s.replace("*", "+").replace("++", " ")

for c in "12346789":
	s = s.replace(c, "1")

while " 00" in s or ' +00' in s:
	s = s.replace(" 00", " 0")
	s = s.replace("+00", " 0")

s = s.replace(" 01", " 1")
s = s.replace(" 05", " 5")
s = s.replace("+01", " 1")
s = s.replace("+05", " 5")

s = s.replace("1+", " ")

while "1 " in s:
	s = s.replace("1 ", " ")

s = s.replace(" +", " ")
s = s.replace("+ ", " ")

a = [c for c in s.split()]

for c in sorted(a, key=len, reverse=1)[:10]:
	print(len(c), c)