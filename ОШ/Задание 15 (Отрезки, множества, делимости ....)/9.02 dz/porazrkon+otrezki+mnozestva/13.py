def f(x):
    return ( ((x in q) and (x not in d))   and   ((x in a) <= (x in p)) )


p = {12, 24, 36, 48, 60}
q = {20, 35, 50, 65, 80, 95}
d = {10, 35, 60, 85, 110, 135, 160}
a = set()

b = []
for x in range(1000):
    if f(x):
        b.append(x)

b.sort()
print(b[0] * b[-1])
