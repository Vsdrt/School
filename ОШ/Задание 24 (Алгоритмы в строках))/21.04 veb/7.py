s = open("24_7.txt").readline()

d = [0] * len(s)
c = ["ABA", "CB", "AC", "BB", "ABC", "BCB", "BA", "AB"]

for i in range(1, len(s)):
	for c1 in c:
		if s[i-len(c1)+1: i+1] == c1:
			d[i] = max(d[i], d[i-len(c1)]) + len(c1)

print(max(d))