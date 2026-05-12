from re import *


s = open("ОШ/Задание 24 (Алгоритмы в строках))/27.04 dz/2 задача/24.txt").readline()
x = f'(?:0|[2345][02345]*)'
pat = f'{x}(?:[+*]{x})+'
a = findall(pat, s)
res = max(a, key = len)
print(len(res), res)