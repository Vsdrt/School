from re import *


s = open("ОШ/Задание 24 (Алгоритмы в строках))/27.04 dz/4 задача/24.txt").readline()

x = '(?:[1-6]+)'
pat = f'B{x}(?:[*-]{x})+'
a = findall(pat, s)
res = max(a, key = len)
print(len(res))