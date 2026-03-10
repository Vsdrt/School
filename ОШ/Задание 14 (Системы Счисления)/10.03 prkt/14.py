def sm(x):
	sm = 0
	for i in x:
		sm += int(i)
	return sm


x = 7*5**1984 - 6*25**777 + 5*125**333 - 4

s = ''
while x > 0:
	s = str(x%5) + s
	x //= 5

print(sm(s))