def f(x, a):
    return (54 <= x <= 75) <= (((25 <= x <= 120) == (54 <= x <= 75)) or ((not 25 <= x <= 120) <= a))


mn = 10000000000
for st in range(0, 200):
    for en in range(st, 200):
        if all(f(x, st <= x <= en) for x in range(500)):
            if mn > en - st:
                mn = en - st
print(mn)
