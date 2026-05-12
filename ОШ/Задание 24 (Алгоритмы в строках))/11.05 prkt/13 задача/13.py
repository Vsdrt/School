from re import findall



s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/13 задача/24.txt').readline()

pat = 'Z[XY](?:Z[XY])*'
res = max(findall(pat, s), key = len)
print(len(res)//2)