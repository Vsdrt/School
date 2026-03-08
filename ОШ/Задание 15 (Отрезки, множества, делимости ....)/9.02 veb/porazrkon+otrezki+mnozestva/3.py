def f(x, a):
    return not(((15 <= x <= 30) <= (not 25 <= x <= 40)) and a and not(10 <= x <= 25))

mxln = 0
for st in range(200):
    for en in range(st, 200):
        if all(f(x, st <= x <= en) for x in range(1000)):
            if mxln < en - st:
                mxln = en - st

print(mxln)
