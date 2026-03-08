for x in "0123456789abcdefghi":
    a = int(f"98{x}79641", 19)
    b = int(f"36{x}14", 19)
    c = int(f"73{x}4", 19)

    if (a + b + c)%18 == 0:
        print(x, (a + b + c)//18)

n = 19 
for x in range(n):
    a = 9*n**7 + 8*n**6 + x*n**5 + 7*n**4 + 9*n**3 + 6*n**2 + 4*n**1 + 1*n**0
    b = 3*n**4 + 6*n**3 + x*n**2 + 1*n**1 + 4*n**0
    c = 7*n**3 + 3*n**2 + x*n**1 + 4*n**0

    if (a + b + c)%18 == 0:
        print(x, (a + b + c)//18)
