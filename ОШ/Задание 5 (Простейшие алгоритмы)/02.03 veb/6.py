def per(x):
    s = ""
    while x > 0:
        s = str(x%6) + s
        x //= 6

    return s


def solve(x):
    a = per(x)
    a = a + a[-1:]
    a = bin(int(a, 6))[2:]
    sm = a.count("1")
    return sm



for n in range(1, 10**5):
    if solve(n) == 18:
        print(n)
    
