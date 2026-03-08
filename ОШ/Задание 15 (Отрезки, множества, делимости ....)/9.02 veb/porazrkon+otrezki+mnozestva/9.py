def f(x):
    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))

p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
q = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31}
a = {2, 6, 8, 12, 14, 18, 20, 24, 26, 30}


for x in range(1000):
    if not f(x):
        print(x)

print(len(a))

