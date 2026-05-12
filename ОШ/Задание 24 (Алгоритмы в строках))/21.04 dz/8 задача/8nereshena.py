with open("ОШ/Задание 24 (Алгоритмы в строках))/21.04 dz/8 задача/24.txt", "r") as f:
    s = f.read().replace("\n", "").replace("\r", "")
print(len(s))

max_len = 0
curr_len = 1

for i in range(1, len(s)):
    if (s[i-1] == 'X' and s[i] == 'Y') or \
       (s[i-1] == 'Y' and s[i] == 'Z') or \
       (s[i-1] == 'Z' and s[i] == 'X'):
        curr_len += 1
    else:
        # Если цепочка не может продолжаться, начинаем заново
        # но сначала проверяем, может ли текущий символ начать новую цепочку
        # или предыдущий+текущий могут начать цепочку из 2 символов
        curr_len = 1
    
    max_len = max(max_len, curr_len)

print(max_len)