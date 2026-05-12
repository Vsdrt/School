s = open("24_3.txt").readline()

for c in "ACD":
	s = s.replace(c, " ")

for c in "23456":
	s = s.replace(c, "1")

s = s.replace("-", "*")
s = s.replace("**", " ")

for c in set(s):
	s = s.replace(c + "B", c + " B")

s = s.replace("B*", " ")

s = s.replace("* ", " ")

a = [c for c in s.split() if c[0] == "B" and "*" in c]

for c in sorted(a, key = len, reverce = 1):
	print(len(c), c)
