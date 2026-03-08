def f(n):
    s = bin(n)[2:] 

    if s[-2] == s[-1]:
        s += "0"
    else:
        s += "1"
    
    if s[-2] == s[-1]:
        s += "0"
    else:
        s += "1"

    return int(s, 2)



for n in range(2, 1000):
    if f(n) > 93:
        print(n)
        break
        
