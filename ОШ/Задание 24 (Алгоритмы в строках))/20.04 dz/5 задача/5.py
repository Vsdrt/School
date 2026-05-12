s = open("ОШ/Задание 24 (Алгоритмы в строках))/20.04 dz/5 задача/24.txt").readline()

res = 0

for i in range(len(s)):
  if s[i] == 'A' or s[i] == 'D':
    for j in range(i + 1, len(s)):
      if s[j] == 'D' or s[j] == 'A':
        cur = s[i:j+1]
        if cur.count('A') == 1 and cur.count('D') == 1:
          res = max(res, len(cur))
        break
print(res)