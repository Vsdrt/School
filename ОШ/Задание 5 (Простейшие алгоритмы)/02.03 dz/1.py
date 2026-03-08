def solve(x):
    a = bin(x)[2:]
    if x%3==0:
        a = a + a[-3:]
    else:
        a = a + bin(3*(x%3))[2:]

    return int(a, 2)

mx = 0

for n in range(1, 100000):
    if solve(n)<=170:
        if solve(n)>mx:
            mx = solve(n)

print(mx)
    
