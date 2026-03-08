def per(x):
    s = ""
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s

def sm(x):
    summ = 0
    for i in x:
        summ += int(i, 3)

    return per(summ)
        

def solve(x):
    a = per(x)
    if x%2 == 0:
        a = "1" + a + "00"
    else:
        a = str(a) + sm(a)

    return int(a, 3)

for n in range(1, 10000):
    if solve(n) > 168:
        print(n)
        break
