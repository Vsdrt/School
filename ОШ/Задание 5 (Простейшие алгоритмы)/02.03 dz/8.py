def solve(x):
    a = bin(x)[2:]
    a = a[1:]

    if a.count("1")%2 == 0:
        a = "10" + a
    else:
        a = "1" + a + "0"

    return int(a, 2)

mx = 0
for n in range(2, 10000):
    if solve(n) < 450:
        if mx < solve(n):
            mx = solve(n)

print(mx)
        
    
