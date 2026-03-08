x = 9**7 + 3**21 - 9
k = 0
s = ""
while x > 0:
    if x%3 == 2:
        k += 1
    s = str(x%3) + s
    x //= 3
print(s.count("2"), k, s)
