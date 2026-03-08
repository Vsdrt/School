def f(x, y, a):
    return (x > 39) or (y > 26) or (2*x + 4*y < a)

a = 0
while True:
    a += 1
    if all(f(x/10, y/10, a) for x in range(200*10) for y in range(200*10)):
        print(a)
        break
