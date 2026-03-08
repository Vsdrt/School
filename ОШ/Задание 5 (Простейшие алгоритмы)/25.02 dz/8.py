def per(x, n):
    x = int(x)
    s = ""
    while x > 0:
        s = str(x%n) + s
        x //= n

    return s


def solve(n):
    s = per(n, 6)
    s = s + s[-1]
    s = int(s, 6)
    s = bin(s)[2:]
    
    return s.count("1")
    



for n in range(1, 10**5+1):
    if solve(n) == 18:
        print(n)
    
