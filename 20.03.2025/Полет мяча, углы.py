import math


def f(u):
    return S * math.tan(u) - ((g * S**2) / (2 * V**2 * (math.cos(u))**2)) - H


H, S, V, g = 2, 10, 12, 9.81
u = 0
EPS = 0.001
DELTA = EPS * 2

while u < math.pi/2:
    if f(u)*f(u + DELTA) <= 0:
        alpha = (u + EPS) * 180 / math.pi
        print("{:4.1f}".format(alpha))
    u += DELTA
