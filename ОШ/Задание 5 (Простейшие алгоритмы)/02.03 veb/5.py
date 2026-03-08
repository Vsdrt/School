def per(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3

    return s


def solve(x):
    a = per(x)
    if x % 5 == 0:
        a = a + a[-3:]
    else:
        a = a + per(5*(x%5))

    return int(a, 3)


mx_n = 0
for n in range(1, 1000):
    if solve(n) < 5496:
        if mx_n < n:
            mx_n = n

print(mx_n)
