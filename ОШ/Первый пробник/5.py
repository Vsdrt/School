for n in range(1, 10000):
    q = str(bin(n)[2:])
    if n % 3 == 0:
        q += q[-3:]
    if n % 3 != 0:
        ost = str(bin(3*(n % 3))[2:])
        q += ost

    r = int(q, 2)
    
    if r >= 200:
        print(n, r, q)
        break
    
