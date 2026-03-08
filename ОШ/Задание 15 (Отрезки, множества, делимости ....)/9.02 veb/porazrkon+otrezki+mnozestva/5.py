def f(x, a):
    return not(((x&17!=0) <= ((x&a!=0) <= (x&58!=0))) <= ((x&8==0) and (x&a!=0) and (x&58==0)))


a = 56
while True:
    a -= 1
    if all(f(x, a) for x  in range(1, 1000)):
        print(a)
        break
