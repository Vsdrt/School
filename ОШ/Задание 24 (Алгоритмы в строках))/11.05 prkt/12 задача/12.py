from re import *



s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/12 задача/24.txt').readline()

pat = '(?:[BC]{2}[A])+'
a = findall(pat, s)
res = max(a, key=len)
print(len(res))