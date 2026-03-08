n = 150
for x in range(n):
    a = 5*n**4 + 1*n**3 + x*n**2 + 2*n**1 + 9*n**0
    b = x*n**3 + 0*n**2 + 2*n**1 + 3*n**0

    if (a+b)%149 == 0:
        print(x, (a+b)//149)
