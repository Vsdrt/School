s = open("ОШ/Задание 24 (Алгоритмы в строках))/21.04 dz/2 задача/24.txt").readline()
print(len(s))
print(s[:50])

l = r = 0
res = 10000000
cp = 0

while r < len(s):
	if s[r] == ".": cp += 1

	while cp >= 7:
		if cp == 7:
			res = min(res, r - l + 1)

		if s[l] == ".": cp -= 1
		l += 1

	r += 1

print(res)
