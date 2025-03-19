import math


def f(x):
    return x**2


L, a, B, h = 0, 0, 10, 0.01
x = a

while x < B:
    y1 = f(x)
    y2 = f(x+h)
    L += math.sqrt(h**2 + (y2 - y1)*(y2 - y1))
    x += h

print(L)

