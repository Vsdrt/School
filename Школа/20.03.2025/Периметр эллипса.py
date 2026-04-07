import math


a = 2; b = 3; h = 0.001
x = a*math.cos(T); y = b*math.sin(T)
P = 0

L = math.pi * (3*(a+b) - math.sqrt((3*a+b)*(a+3*b)))
print(f'Периметр заданного эллипса по формуле Рамануджана = {L}')

while x < b:
    P += f(x, y) + f(x + h, y + h)
    x += h
    y += h

print(P)