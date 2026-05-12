from re import *


s = open('24.txt').readline()

x = "(?:0|[1-9][0-9]*[05])"
pat = f'{x}(?:[+*]{x})+'
a = findall(pat, s)
res = max(a, key=len)
print(len(res), res)