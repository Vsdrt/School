a = [int(x) for x in open("ОШ/Задание 17 (Последовательности)/2.04 prkt/2.txt")]
q = 0
w = 0
mn = 10**10
mx = 0

for i in a:
	if i % 17 == 0:
		q += 1 
		if i > mx:
			mx = i
	if i % 11 == 0:
		w += 1 
		if i < mn:
			mn = i

if w > q:
	print(w, mn)
else:
	print(q, mx)