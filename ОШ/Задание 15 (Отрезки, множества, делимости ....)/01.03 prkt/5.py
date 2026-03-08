def f(x, a):
    d = (17 <= x <= 58)
    c = (29 <= x <= 80)
    return d <= (((not c) and (not a)) <= (not d))

mn = 10**10
for st in range(0, 200):
    for en in range(st, 200):
        if all(f(x/4, st <= x/4 <= en) for x in range(-100*4, 100*4)):
            if mn > en - st:
                mn = en - st

print(mn)
