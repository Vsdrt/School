def f(x, a):
    return ((x%84!=0) or (x%90!=0)) <= (x%a!=0)

print("otvet", end = " ")
a = 0
while True:
    a += 1
    if all(f(x, a) for x in range(1, 1000000)):
        print(a)
        break
