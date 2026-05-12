s = open("24_1.txt").replace()
print(len(s))

l = r = 0
res = 0
count_t = 0

while r < len(s):
	if s[r] == "T":
		count_t += 1

	while count_t > 100:
		if s[l] == "T":
			count_t -= 1
		l += 1

	if count_t == 100:
		res = max(res, r - l + 1)

	r += 1

print(res)