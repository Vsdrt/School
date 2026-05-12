s = open('ОШ/Задание 24 (Алгоритмы в строках))/11.05 prkt/3 задача/24.txt').readline()

res = 1 
mx = 0 

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        res += 1
    else:
        mx = max(res, mx)
        res = 1
print(mx) # выводим результат

