def f(x):
    q = {1, 2, 4, 8, 16}
    w = {3, 4, 9, 16}
    a = set()
    return (x not in q) and (x not in w) or (x in a)

for x in range(1000):
    if not f(x):
        print(x)
