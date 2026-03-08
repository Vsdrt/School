x = 2**24 + 2**14 - 2**5

s = ""
while x > 0:
    s = str(x%2) + s
    x //= 2

print(s.count("1"))
