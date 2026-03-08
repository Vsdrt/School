def f(x, a):
    b = (24 <= x <= 90)
    c = (47 <= x <= 115)
    return c <= ((not(a) and (b)) <= (not c))

mn = 10**10
for st in range(0, 500):
    for en in range(st, 500):
        if all(f(x, st <= x <= en) for x in range(-200, 200)):
            if mn > en - st:
               mn = en - st

print(mn)
