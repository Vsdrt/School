def solve(x):
    a = bin(x)[2:]
    if a.count("1")%2 == 0:
        a = "1" + a[:-2] + "10"

    else:
        a = "10" + a[2:] + "1"

    return int(a, 2)


for n in range(1, 100000):
    if solve(n) > 202:
        print(n, solve(n))
    
