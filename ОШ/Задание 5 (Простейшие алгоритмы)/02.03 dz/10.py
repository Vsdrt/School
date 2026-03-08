def per(x, n):
    digits = []
    while x > 0:
        digits.append(x%n)
        x //= n
    return digits


def summ(x):
    s = 0
    for i in x:
        s += int(i)
    return s


def solve(x):
    s = ""
    for n in range(2, 33):
        a = per(x, n)
        s += str(a.count(n-1))
    return summ(s)


res = set()
for n in range(100, 1000):
    res.add(solve(n))

print(len(res))
    
