from re import *

s = open("24.txt").readline()

x = '(?:[789]+)'
pat = f'{x}(?:[+]{x})+'
a = findall(pat, s)

res = 0
for c in a:
	res = max(eval(c), res)

print(res)