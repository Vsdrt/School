for x in range(1, 2031):
    a1 = a = 6**260 + 6**160 + 6**60 - x
    k = 0
    s = ''
    while a > 0:
        if a%6 == 0:
            k += 1
        s = str(a%6) + s
        a  //= 6

    if k == 202:
        print(x)
        break

    
