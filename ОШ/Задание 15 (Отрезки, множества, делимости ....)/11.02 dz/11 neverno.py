def f(x, a):
    return (((x**2 + x - 20 >= 0) or a) and ((x**2 - 3*x - 18 <= 0) or a))



mn = 10**10

for st in range(3000):
    for en in range(st, 3000):
        k = 0
        if all(f(x, st <= x <= en) for x in range(1000)):
            k += 1
            if k == 10:
                if en - st < mn:
                    mn = en - st
                


print(mn)
