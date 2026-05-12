s = open("ОШ/Задание 24 (Алгоритмы в строках))/28.04 dz/2 задача/24.txt").readline()

r = l = 0
res = 0
ct = 0

while r < len(s):
	if s[r] == ".": ct += 1

	while ct > 5:
		if s[l] == ".": ct -= 1
		l += 1

	if ct <= 5:
		res = max(res, r - l + 1)
	
	r += 1

print(res)