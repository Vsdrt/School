def f(x, y, a):
    return (2*x + 3*y != 150) or (x < a) and (y < a)


a = 0
while True:
    a += 1
    if all(f(x, y, a) for x in range(1000) for y in range(1000)):
        print(a)
        break
