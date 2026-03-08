for x in "0123456789abcdef":
    a = int(f"b7a{x}9", 16)
    b = int(f"54{x}ed", 16)

    c = a + b
    s = ''
    while c > 0:
        s = str(c%6) + s
        c //= 6
        
    if sum(map(int, s)) == 25:
        print(x, a+b)
        
        
        

    
        
