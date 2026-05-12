f = open('ОШ/Задание 26 (Сортировка данных)/30.04 dz/4 задача/26.txt')
n = int(f.readline())

a = {}

for i in range(n):
	r, p = map(int, f.readline().split())

	if r in a:
		a[r] += [p]
	else:
		a[r] = [p]

def f():
	for r in sorted(a.keys()):
		a[r].sort()
		b = a[r]
		if len(b) > 4:
			for i in range(len(b) - 4):
				x = b[i:i+5]
				if sum(x) / 5 == float(b[2]):
					print(r, b[-1])
					return 

f()