def f(x, a):
    return ((a) and ((100<= x <= 234) or ((100 <= x <= 234) or (10 <= x <= 269)) and ((100 <= x <= 234) <= (10 <= x <= 269)))) or (a <= (10 <= x <= 269))


mx = 0

for st in range(500):
    for en in range(st, 500):   
        if all(f(x, st <= x <= en) for x in range(1000)):
            if mx < en - st:
                mx = en - st

print(mx)
            
