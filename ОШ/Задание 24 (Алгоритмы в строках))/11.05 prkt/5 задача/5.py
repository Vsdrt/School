s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/5 задача/24.txt').readline()

r = l = res = 0
cd = 0

while r < len(s):
	if s[r-1:r+1] == "CD": cd += 1

	while cd > 160:
		if s[l:l+2] == "CD": cd -= 1
		l += 1

	if cd == 160:
		res = max(res, r - l + 1)
	
	r += 1

print(res)
