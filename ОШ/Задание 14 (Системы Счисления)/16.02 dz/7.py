x = 3*625**173 + 4*125**180 + 3*25**157 + 2*5**155 + 156

k = 0
s = ""
d = "0123456789abcdefghijklmnopqrstuvwxyz"
while x > 0:
    if x%25 == 0:
        k += 1
    s = d[x%25] + s
    x //= 25

print(s, s.count("0"), k)
