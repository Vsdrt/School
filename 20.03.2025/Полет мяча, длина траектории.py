import math


def f(x, u, V, g):
    return x * math.tan(u) - ((g * x ** 2) / (2 * V ** 2 * (math.cos(u)) ** 2))

V = 12; g = 9.81
L = 0 ; a = 0; b = 10; h = 0.0001

x = a
u = math.radians(65.8)

while x < b:
    y1 = f(x, u, V, g)
    y2 = f(x + h, u, V, g)
    L += math.sqrt(h ** 2 + (y2 - y1)**2)
    x += h

print(L)
