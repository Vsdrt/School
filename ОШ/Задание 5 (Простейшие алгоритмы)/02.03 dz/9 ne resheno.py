def per(x, n):
    s = ""
    while x > 0:
        s = str(x%n) + s
        x //= n
    return s


def solve(x):
    
    a = per(x, 3)
    if a.count("1")%2==0:
        a = int(a, 3)
        a = per(a, 4)
        a = "3" + a + "00"
    else:
        a = int(a, 3)
        a = per(a, 4)
        a = "12" + a

    a = int(a, 4)
    a = per(a, 5)
    if a.count("4") == a.count("2"):
        a = int(a, 5)
        a = per(a, 6)
        a = a + "222"
    else:
        a = int(a, 5)
        a = per(a, 6)
        a = "5" + a + "4"
        
    a = int(a, 6)
    a = per(a, 7)
    if a.count("0")>a.count("5"):
        a = int(a, 7)
        a = per(a, 9)
        a = "4" + a
    else:
        a = int(a, 7)
        a = per(a, 9)
        a = "123" + a[3:] + a[:-2] + "87"

    return int(a, 9)

print(solve(234))


mx = 0
for n in range(101, 100_000):
    if mx < solve(n):
        mx = solve(n)

print(mx)


    
