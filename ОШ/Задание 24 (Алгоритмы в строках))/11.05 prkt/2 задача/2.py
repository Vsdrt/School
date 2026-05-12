from re import *



s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/2 задача/24.txt').readline()
print(s[:100])

x = '(?:0|[1-9][0-9]*)'
pat = f'{x}(?:[*-]{x})+'
res = max(findall(pat, s), key = len)
print(res, len(res))