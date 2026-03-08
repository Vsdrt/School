def per(x):
    s = ""
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s

def solve(x):
    a = str(per(x))
    if a.count("2") + a.count("0") > a.count("1"):
        a = "22" + a
    else:
        a = "11" + a

    return int(a, 3)

res = set()

for n in range(11, 1000):
    if solve(n) > 100:
        res.add(solve(n))

print(min(res))
