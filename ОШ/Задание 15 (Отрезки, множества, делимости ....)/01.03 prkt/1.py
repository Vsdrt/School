def tr(x, y, z):
    if x < y + z and  y < x + z and z < x + y:
        return True
    else:
        return False

def mx(x, y):
    if x > y:
        return x
    else:
        return y

def f(x, a):
    return not((tr(x, 11, 18)==(not(mx(x, 5) > 68))) and tr(x, a, 5))


a = 0

while True:
    a += 1
    if all(f(x, a) for x in range(1, 100000)):
        print(a)
