def f(x, a):
    return not((not(15 <= x <= 30) or (15 <= x <= 60)) and a)


for st in range(100):
    for en in range(st, 100):
        if all(f(x, st <= x <= en)for x in range(100)):
            print(st, en)

print("otvet 0")
