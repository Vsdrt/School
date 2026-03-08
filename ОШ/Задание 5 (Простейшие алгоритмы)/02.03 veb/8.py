def solve(x):
    a = bin(x)[2:]
    ps = a[-1]
    
    if ps == "0":
        ps = "1"
    else:
        ps = "0"
        
    a = a[:-1] + ps

    a = a + str((a.count("1")%2))
    return int(a, 2)


for n in range(1, 1000000):
    if solve(n) > 78:
        print(n, solve(n))

