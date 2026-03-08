def f(x, a):
    return (a%3==0) and ((220%x==0) <= ((a%x!=0) <= (550%x!=0)))


a = 0
while True:
    a += 1
    if all(f(x, a) for x in range(1, 100000)):
        print(a)
        break
