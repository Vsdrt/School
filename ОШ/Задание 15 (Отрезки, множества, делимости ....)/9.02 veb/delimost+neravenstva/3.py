def f(x, a):
    return (a % 12 == 0) and ((530 % x == 0) <= ((a % x != 0) <= (170 % x !=0)))

k = 0
for a in range(1, 1001):
    if all(f(x, a) for x in range(1, 100000)):
        k += 1
print(f"otvet {k}")

