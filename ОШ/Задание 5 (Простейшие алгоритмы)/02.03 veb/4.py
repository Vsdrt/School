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
    if x%2==0:
        a = a + a[-2:]
    else:
        a = a + sm(a)

    return int(a, 3)


print(solve(10), solve(11))


mn = 10**10
n_mn = 0

for n in range(1, 1000):
    if n > 9:
        if mn > solve(n):
            mn = solve(n)
            n_mn = n
        

print(n_mn)
        
