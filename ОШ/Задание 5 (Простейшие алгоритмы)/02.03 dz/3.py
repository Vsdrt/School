def solve(x):
    a = bin(x)[2:]
    if x%2 == 0:
        a = a + "10"
    else:
        a = "1" + a + "01"

    return int(a, 2)

for n in range(1, 100000):
    if solve(n) > 516:
        print(n, solve(n))
        break
