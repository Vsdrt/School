x = 7**202 + 49**102 - 7**20

s = ""
while x > 0:
    s = str(x%7) + s
    x //= 7

print(s.count("6"))
