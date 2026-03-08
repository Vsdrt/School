def f(x, a):
    return ((x%a ==0) and (x%21==0)) <= (x%18==0)


a = 0
while True:
    a += 1
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
        break
