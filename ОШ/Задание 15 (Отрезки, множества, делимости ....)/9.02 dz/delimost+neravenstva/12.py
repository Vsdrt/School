def f(x, a):
    return (x + a >= 160) or (x%7==0) <= (x+(-17) <= 0)


a = 0
while True:
    a += 1
    if all(f(x, a) for x in range(1, 1000000)):
        print(a)
        break
