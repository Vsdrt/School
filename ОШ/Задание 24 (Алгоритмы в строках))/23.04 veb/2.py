s = open("24_2.txt").readline()

s = s.replace("*", " ")
s = s.replace("++", " ")

s = s.replace(" +", " ")
s = s.replace("+ ", " ")

a = [c for c in s.split() if "+" in c]
res = 0

for c in a:
	res = max(res, eval(c))

print(res)