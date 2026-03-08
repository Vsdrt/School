def solve(n):

    s = bin(n)[2:]

    if s.count("1") % 2 == 0:
        s = s + "1"
        s = s[2:]
        s = "10" + s
    else:
        s = s + "11"
        s = s[2:]
        s = "1" + s

    return int(s, 2)

for n in range(1, 10000):
    if solve(n) >= 100:
         print(n, solve(n))
         break
