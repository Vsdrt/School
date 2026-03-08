def f(x, a):
    return ((a) <= (43 <= x <= 49)) or (44<= x <=53)

mx = 0
for st in range(300):
    for en in range(st, 300):
        if all(f(x, st <= x <= en) for x in range(1, 1000)):
            if mx < en - st:
                mx = en - st

print(mx)
