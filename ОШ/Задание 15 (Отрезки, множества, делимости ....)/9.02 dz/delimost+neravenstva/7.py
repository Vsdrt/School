def f(x, a):
    return (x%a != 0) <= ((x%6==0) <= (x%9!=0))

a = 1000000
while True:
    a-=1
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
        break
