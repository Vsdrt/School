s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/10 задача/24.txt').readline()

s = "XYZ"
alf = {
	'X': 1,
	'Y': 2,
	'Z': 3
}

res = 1
mx = 0

for i in range(len(s) - 1):
	if alf[s[i]] <= alf[s[i+1]]:
		res += 1
	else:
		mx = max(res, mx)
		res = 1

mx = max(res, mx) 

print(mx)

