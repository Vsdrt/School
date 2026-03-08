def r(n):
    s = bin(n)[2:]

    if n % 2 == 0:
        s = s + s[-2:]
    else:
        s = "1" + s + "1"


    return int(s, 2)
    




for n in range(1, 10000):
    if r(n) > 100:
        print(n)
        break
    
