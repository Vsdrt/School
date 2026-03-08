def f(x):
    return ((x in p) <= (((x in q) and (x not in a)) <= (x not in p)))

p = {2, 4, 6, 8, 10, 12}
q = {4, 8, 12, 116}
a = set()

sm = 0

for x in range(1, 10000):
    if not f(x):
        sm += x
        
print(sm)
