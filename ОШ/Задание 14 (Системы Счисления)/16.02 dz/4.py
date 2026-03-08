n = 15
for x in range(n):
    a = int(f"97531{x}19", n)
    b = int(f"3{x}519", n)
    if (a+b)%11 == 0:
        print(x, (a+b)//11)
       
