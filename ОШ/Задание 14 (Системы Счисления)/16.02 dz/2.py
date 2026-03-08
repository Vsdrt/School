x = 7*729**543 - 6*81**765 - 5*9**987 - 20
s = ""
k = 0
while x > 0:
    if x%9 == 8:
        k += 1
    s = str(x%9) + s
    x //= 9

print(k, s, s.count("8"))
