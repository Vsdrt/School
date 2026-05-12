s = open("24_6.txt").readline()

s = s.replace("--", " ")

a = [c for c in s.split()]

res = 0

for c in a:
	if not c.strip("-"):
		continue

	x = list(map(int, c.strip("-").split("-")))

	sumi = 0
	l = 0

	for r in range(len(x)):
		sumi += x[r]
		leni += len(str(x[r]))

		while sumi - x[l] * 2 >= 20000:
			sumi -= x[l]
			leni -= len(str(x[l]))
			l += 1

		res = max(leni + r - l, res)

print(res)