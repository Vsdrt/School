def solve(x):
    a = bin(x)[2:]

    a = a + str((a.count("1"))%2)
    a = a + str((a.count("1"))%2)

    return int(a, 2)


for n in range(1, 100000):
    if solve(n) > 452:
        print(solve(n))
