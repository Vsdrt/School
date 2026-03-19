def simple(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


k = 0
for x in range(1547341, 1547410):
    if simple(x):
        k += 1
        print(k, x)
