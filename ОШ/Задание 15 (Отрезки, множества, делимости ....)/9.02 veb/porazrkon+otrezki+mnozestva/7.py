def f(x):
    return not ((x not in a) <= (((x not in p) and (x in q)) or (x not in q)))

p = {1, 2, 3, 4, 5, 6}
q = {3, 5, 15}
a = set()

for x in range(1, 100):
    if f(x):
        print(x)


