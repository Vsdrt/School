def f(x, a):
    return ((not 13 <= x <= 19) and (not 17 <= x <= 23)) <= (a <= ((not 17 <= x <= 23) <= (13 <= x <= 19)))

mx = 0

for st in range(1, 200):
    for en in range(st, 200):
        if all(f(x, st <= x <= en) for x in range(1000)):
            if mx < en - st:
                mx = en - st
                print(st, en)

print(mx)
            

