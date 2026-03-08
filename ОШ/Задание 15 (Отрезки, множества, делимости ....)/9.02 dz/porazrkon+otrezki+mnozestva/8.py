def f(x):
    return (x not in a) <=((x not in {1, 2, 4, 8}) and (x not in {1, 2, 3, 4, 5, 6}))

a = set()

for x in range(0, 100):
    if not f(x):
        print(x)
