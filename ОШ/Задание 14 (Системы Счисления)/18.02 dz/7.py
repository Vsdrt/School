for x in range(2, 1000):
    a = 1234**999 + 453**998 + 123**997 + 435
    k = 0
    while a > 0:
        if a % x == 0:
            k += 1
        a //= x

    if k == 25:
        print(x)
        break
