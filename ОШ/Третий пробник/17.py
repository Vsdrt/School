a = [int(x) for x in open("ОШ/Третий пробник/17.txt")]
res = []

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        x, y = a[i], a[j]
        if (x % 160 != y % 160) and (x % 7 == 0 or y % 7 == 0):
            res += [x + y]

print(len(res), max(res))
