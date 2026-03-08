def f(x, a):
    return ((x%175==0) <= (x%25!=0)) or (2*x + a >= 1780)

a = 0
while True:
    a += 1
    if all(f(x, a) for x  in range(1, 1000000)):
        print(a)
        break
