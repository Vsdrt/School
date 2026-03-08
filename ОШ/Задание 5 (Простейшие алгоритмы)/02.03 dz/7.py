def per(x):
    s = ""
    while x > 0:
        s = str(x%3) + s
        x //= 3

    return s

def solve(x):
    a = per(x)
    if x%3 == 0:
        a = "1" + a + "02"
    else:
        a = a + per(4*(x%3))

    return int(a, 3)


for n in range(1, 1000000):
    if solve(n) < 199:
        print(n)
