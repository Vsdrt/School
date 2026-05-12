s = open("ОШ/Задание 24 (Алгоритмы в строках))/23.04 dz/1 задача/24.txt").readline()

for i in "12349":
	s = s.replace(i, "1")

s = s.replace("-", "*")
s = s.replace("**", " ")



while " 00" in s or "*00" in s:
	s = s.replace(" 00", " 0")
	s = s.replace("*00", " 0")

s = s.replace("*01", " 1")
s = s.replace(" 01", " 1")

s = s.replace(" *", " ")
s = s.replace("* ", " ")

print(s[:100])


a = s.split()
for i in sorted(a, key=len, reverse=1)[:5]:
	print(len(i), i)
