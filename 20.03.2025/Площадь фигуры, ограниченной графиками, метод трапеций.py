import math


def f1(x):
    return x**2
def f2(x):
    return 4 * math.cos(x)


a = -1.2; b = 1.2; h = 0.0001
S = 0
x = a

while x < b:
    S += f1(x) - f2(x) + f1(x+h) - f2(x+h)
    x += h

S *= h/2
print(abs(S))
