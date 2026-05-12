from re import *


s = open("ОШ/Задание 24 (Алгоритмы в строках))/27.04 dz/5 задача/24.txt").readline()
x = '(?:0|[1-9][0-9]*)'
pat = f'AFD{x}(?:[+*]{x})+'
a = findall(pat, s)
print(len(max(a, key = len)))