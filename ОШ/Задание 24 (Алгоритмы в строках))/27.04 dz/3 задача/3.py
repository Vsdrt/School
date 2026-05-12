from re import *
from math import prod

s = open('ОШ/Задание 24 (Алгоритмы в строках))/27.04 dz/3 задача/24.txt').readline()
x = f'(?:0|[1-7][0-7]*)'
pat = f'F{x}(?:[+*]{x})+'
a = findall(pat, s)

mx_len = len(max(a, key = len))
res = 0

for st in a:
	if len(st) == mx_len:
		sm = 0 

		st = st[1:]
		wrs = st.split("+")
		
		for wr in wrs:
			if wr.count("*")>=1:
				chs = wr.split("*")
				new_chs = []
				for ch in chs:
					new_chs += [int(ch, 8)]

				sm += prod(ch for ch in new_chs)
				
			else:
				sm += int(wr, 8)
		sm = max(sm, res)

print(sm)

