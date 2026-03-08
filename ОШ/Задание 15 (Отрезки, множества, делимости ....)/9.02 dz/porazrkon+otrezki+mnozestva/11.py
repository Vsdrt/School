def f(x):
    return (x not in a) <= ((x not in {1, 12}) and (x not in {12, 13, 14, 15, 16}))

a = set()

for x in range(1000):
    if not f(x):
        print(x)
