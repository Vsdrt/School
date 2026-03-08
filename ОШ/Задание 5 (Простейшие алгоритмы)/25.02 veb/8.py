def solve(n):

    s = bin(n)[2:]

    if n % 11 == 0:
        s = s + "0"*s.count("0")
    else:
        s = "1"*s.count("1") + s

    return int(s, 2)


for n in range(1, 10000):
    if solve(n)%227 == 0:
        print(n)
        break
