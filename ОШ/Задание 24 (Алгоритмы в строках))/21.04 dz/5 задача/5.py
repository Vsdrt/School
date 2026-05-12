s = open("ОШ/Задание 24 (Алгоритмы в строках))/21.04 dz/5 задача/24.txt").readline()
print(s[:50])

cx = cy = ca = 0
res = 0
r = l = 0

while r < len(s):
	if s[r] == "X": cx += 1
	if s[r] == "Y": cy += 1
	if s[r] == "A": ca += 1

	while cx > 1 or cy > 1 or ca > 0:
		if s[l] == "X": cx -= 1
		if s[l] == "Y": cy -= 1
		if s[l] == "A": ca -= 1
		l += 1

	if cx == 1 and cy == 1 and ca == 0:
		res = max(res, r - l + 1)
	
	r += 1

print(res)