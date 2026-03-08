def f(x, y, a):
    return (7*y + x < a) or (2*x + 3*y > 98)

a = 0
while True:
    a += 1
    if all(f(x, y, a) for x in range(1, 2000) for y in range(1, 2000)):
        print(a)
        break
