def f(x):
    return ((1) <= (x in p)) and ((x in q) <= (0))


p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {5, 10, 15, 20, 25, 35, 40, 45, 50}
a = set()
b = set()

for x in range(1000):
    if f(x):
        b.add(x)

print(len(b))
