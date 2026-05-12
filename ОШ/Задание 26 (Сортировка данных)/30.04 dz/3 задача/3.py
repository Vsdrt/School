f = open('ОШ/Задание 26 (Сортировка данных)/30.04 dz/3 задача/26.txt')
n = int(f.readline())

a = {}

for i in range(n):
	r, p = map(int, f.readline().split())

	if r in a:
		a[r] += [p]
	else:
		a[r] = [p]

res = 10**20
res_r = 0

for r in sorted(a.keys(), reverse=True):
	a[r].sort()
	b = a[r]
	if len(b) > 1:
		for i in range(len(b)- 1):
			if b[i+1] - b[i] < res:
				res = b[i+1] - b[i] - 1
				res_r = r
				
print(res_r, res)