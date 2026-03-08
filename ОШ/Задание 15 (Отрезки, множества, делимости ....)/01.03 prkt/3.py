def f(x, y, a):
    return ((a < x) or ((x**2 - 7*x + 10) > 0))\
           and ((a >= y) or ((y**2 + 7*y + 12)>0))

a = -100
while True:
    a += 1
    if all(f(x, y, a) for x in range(-500, 500) for y in range(-500, 500)):
        print(a)
