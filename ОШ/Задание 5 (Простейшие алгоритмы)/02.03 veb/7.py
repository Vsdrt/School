def solve(x):
    a = bin(x)[2:]
    if x%5==0:
        a = a + bin(5)[2:]
    else:
        a = a + "1"

    if int(a, 2)%7 == 0:
        a = a + bin(7)[2:]
    else:
        a = a + "1"

    return int(a, 2)

print(solve(10))



n_mx = 0
for n in range(1, 1000000):
    if solve(n) < 1855663:
        if n_mx < n:
            n_mx = n

print(n_mx)
