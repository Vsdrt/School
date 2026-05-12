from re import * 

s = open("24.txt").readline()

x = '(?:[1-6]+)'
pat = f'B{x}(?:[-*]{x})+'
a = findall(pat, s)

res = max(a, key = len)
print(len(res), res)