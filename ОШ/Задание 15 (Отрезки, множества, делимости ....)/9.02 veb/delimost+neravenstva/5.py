def f(x, y, a):
    return ((2*y+x)!=70) or (x < y) or (a < x)

print("otvet", end = " ")
a = 1000
while True:
    a -= 1
    if all(f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        break
