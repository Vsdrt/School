def f(x, y, a):
    return (x<9) <= ((5*y < x) <= (2*x*y < a))

a = 0
while True:
    a += 1
    if all(f(x, y, a) for x in range(1, 5000) for y in range(1, 5000)):
        print(a)
        break
