def f(x ,y, a):
    return (((x - 20) < a) and ((20 - x) < a)) or (x*y > 50)

print("otvet", end = " ")

a = 0
while True:
    a += 1
    if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break

