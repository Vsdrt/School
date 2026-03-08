for x in "0123456789abcdef":
    a = int(f"b7a{x}9", 16)
    a += int(f"54{x}ed", 16)
    q = a

    s = ""
    while a > 0:
        s = str(a%6) + s
        a //= 6

    if sum(map(int, s)) == 25:
        print(x, q)
        
