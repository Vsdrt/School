def solve(x):
    a = bin(x)[2:]

    if x%2 == 0:
        a = "1" + a + "00"
    else:
        a = "10" + a + "1"

    return int(a, 2)


for n in range(1, 10000):
    if solve(n) < 1000:
        print(n, solve(n))
