def solve(x):
    a = bin(x)[2:]
    if (a.count("0") + a.count("1"))%2==0:
        a = a[:(len(a)//2)] + "000" + a[(len(a)//2):]
    else:
        a = "1" + a + "01"

    return int(a, 2)


for n in range(1, 100):
    if solve(n) > 100:
        print(n)
        break
