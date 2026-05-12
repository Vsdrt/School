s = open("ОШ/Задание 24 (Алгоритмы в строках))/21.04 dz/6 задача/24.txt").readline()
print(s[:50])

cr = ca = 0
res = 0
r = l = 0

while r < len(s):
	if s[r] == "R": cr += 1
	if s[r] == "A": ca += 1

	while ca > 3:
		if s[l] == "A": ca -= 1
		l += 1

	if r >= 2 and ca <= 3:
		res = max(res, r - l + 1)
	r += 1

print(res)