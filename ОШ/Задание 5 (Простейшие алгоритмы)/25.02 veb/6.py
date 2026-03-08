def per(x):
    
    s = ""
    n = 3
    
    while x > 0:
        s = str(x%n) + s
        x //= n
    return s


def solve(n):
    
    s = per(n)

    if n % 3 == 0:
        s = s + s[-2:]
    else:
        s = s + per(5*(n%3))

    return int(s, 3)



mn = 10**10

for n in range(1, 10000):
    if solve(n)>133:
        mn = min(solve(n), mn)

print(mn)
            
        
