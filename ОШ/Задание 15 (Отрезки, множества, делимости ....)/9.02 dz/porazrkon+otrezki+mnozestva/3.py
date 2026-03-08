def f(x, a):
    return ((a) and (not 45 <= x <= 68)) <= ((15 <= x <= 33) or (45 <= x <= 68))

ma = 0
for st in range(200):
    for en in range(st, 200):
        if all(f(x, st <= x <= en) for x in range(1, 200)):
            if ma < en - st:
                ma = en - st

print(ma)
