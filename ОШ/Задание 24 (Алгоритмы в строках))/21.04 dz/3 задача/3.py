s = open("ОШ/Задание 24 (Алгоритмы в строках))/21.04 dz/3 задача/24.txt").readline()
print(len(s))

l = r = 0
res = 0
cy = cp = 0

while r < len(s):
	if s[r] == "Y": cy += 1
	if s[r] == ".": cp += 1

	while cy > 0 or cp > 5:
		if s[l] == "Y": cy -= 1
		if s[l] == ".": cp -= 1
		l += 1

	if cy == 0 and cp <= 5:
		res = max(res, r - l + 1)

	r += 1

print(res)