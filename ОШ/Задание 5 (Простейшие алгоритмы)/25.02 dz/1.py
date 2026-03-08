def solve(n):

    s = bin(n)[2:]
    
    sm = s.count("1")
    s = s + str(sm%2)

    sm = s.count("1")
    s = s + str(sm%2)

    return int(s, 2)


for n in range(1, 10000):
    if solve(n) < 50:
        print(solve(n))
