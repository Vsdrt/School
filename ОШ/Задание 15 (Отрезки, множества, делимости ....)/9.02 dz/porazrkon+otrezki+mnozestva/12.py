def f(x, a):
    return ((x&1337 == 0) and ((x&8 != 0) or ((x&a != 0) or not(a&228 == 0))))

k = 0
for a in range(1, 101):
    if all(not f(x, a) for x in range(1, 100000)):
        k += 1
print(k)
