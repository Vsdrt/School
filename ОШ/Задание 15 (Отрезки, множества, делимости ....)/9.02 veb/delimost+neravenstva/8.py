def f(x, y, a):
    return (7*y + 5*x < 1000) or (x < y) or (a < x)

print("otvet", end = " ")

a = 300
while True:
    a -= 1
    if all(f(x, y, a) for x in range(500) for y in range(500)):
        print(a)
        break



