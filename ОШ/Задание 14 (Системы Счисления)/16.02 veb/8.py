for p in range(5, 100):
    for q in range(6, 100):
        a = 2*p**2 + 3*p**1 + 4*p**0
        b = 3*q**2 + 4*q**1 + 5*q**0
        if a == b:
            print(a)
