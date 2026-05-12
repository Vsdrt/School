f = open('26.txt')
n = int(f.readline())

a = {}

for i in range(n):
	r, p = map(int, f.readline().split())
	if r in a:
		a[r] += [p]
	else:
		a[r] = [p]

def f():
	for r in sorted(a.keys(), reverse=True):
		a[r].sort()
		b = a[r]
		for i in range(1, len(b)):
			if b[i] - b[i - 1] == 3:
				print(r, b[i - 1] + 1)
				return 
			
f()
	
