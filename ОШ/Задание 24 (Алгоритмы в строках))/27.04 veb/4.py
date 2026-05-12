from re import *

s = open("24.txt").readline()

x = f'(?:0|[1-5][0-5]*)'
pat = f'{x}(?:[+*]{x})+'
a = findall(pat, s)
res = max(a, key = len)
print(len(res), res)