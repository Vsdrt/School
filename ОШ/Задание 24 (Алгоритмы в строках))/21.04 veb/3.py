s = open("24_3.txt").readline()

l = r = 0
res = 0
cy = 0

while r < len(s):
	if s[r] == "Y": cy += 1

	while cy > 150:
		if s[l] == "Y": cy -= 1
		l += 1

	if cy <= 150:
		res = max(res, r - l + 1)

	r += 1

print(res)