def per(x):
    s = ""
    while x > 0:
        s = str(x%3) + s
        x //= 3

    return s

def summ(x):
    s = 0
    for i in x:
        s = s + int(i, 3)

    return per(s)
    
    

def solve(x):
    a = per(x)

    if x%2 == 0:
        a = "1" + a + '00'
    else:
        a = a + summ(a)

    return int(a, 3)


for n in range(1, 100000):
    if solve(n) > 168:
        print(n)
        
