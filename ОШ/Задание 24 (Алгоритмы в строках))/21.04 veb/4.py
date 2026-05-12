s = open("24_4.txt").readline()
print(len(s))

l = r = 0
res = 0
x = 0

while r < len(s):
	if s[r-2:r+1] == "FAT": x += 1
	if s[r-2:r+1] == "BAD": x += 1

	while x >= 3:
		if s[l:l+3] == "FAT": x -= 1
		if s[l:l+3] == "BAD": x -= 1
		l += 1

		if x == 3:
			res = min(res, r - l + 1)

	r += 1

print(res)