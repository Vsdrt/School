from re import *


s = open('ОШ/Задание 24 (Алгоритмы в строках))/27.04 dz/1 задача/24.txt').readline()
x = '(?:0|[1-9][0-9]*)'
pat = f'{x}(?:[+*]{x})+'
a = findall(pat, s)
res = max(a, key = len)
print(eval(res))