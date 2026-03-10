from fnmatch import fnmatch


def sm(x):
	sm = 0
	x = str(x)
	for i in x:
		sm += int(i)
	return sm


x1 = "*0??3*" 
x2 = "*4??2"
x3 = "*1*"
k = 0
for x in range(700_001, 100000000000):
	if x%13==0 and not(fnmatch(str(x), x1)) and k <= 4 and\
		  not(fnmatch(str(x), x2)) and not(fnmatch(str(x), x3)):
		print(x, sm(x))
		k += 1
	if k == 5:
		break

