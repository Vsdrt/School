def solve(n):

    s = bin(n)[2:]
    for q in range(3):
        if s.count("0") == s.count("1"):
            s = s + s[-1]
        else:
            if s.count("0") > s.count("1"):
                s = s + "1"
            else:
                s = s + "0"

    return int(s, 2)


for n in range(80, 1000):
    if solve(n)%4==0:
        print(n)
        break
        
    
    

    
