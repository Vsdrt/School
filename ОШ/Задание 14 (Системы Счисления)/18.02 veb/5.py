for x in range(10000, 1, -1):
    a = 6**900 + 6**10 - x
    
    s = ""
    while a > 0:
        s = str(a%6) + s
        a//=6

    if s.count("3") == s.count("5"):
        print(x)
        break

        
        
