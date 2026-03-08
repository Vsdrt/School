def f(x, a):
    return (x&41==0) <= ((x&119!=0) <= (x&a!=0))


a = 0
while True:
    a += 1
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
        break
