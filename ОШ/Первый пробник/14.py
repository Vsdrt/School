for x in range(3000, 0, -1):
    q = 9 * 11**210 + 8 * 11**150 - x

    s = ''
    d = "0123456789a"
    while q > 0:
        s = d[q%11] + s
        q = q // 11

    if s.count("0") == 60:
        print(x)
        break
    
