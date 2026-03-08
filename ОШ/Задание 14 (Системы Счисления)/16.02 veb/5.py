n = 24
for x in range(24):
    a = int("4m0f", 24) + x*24**1
    b = int("265afdn0", 24) + x*24**0
    c = int("n40931b3l", 24) + x*24**6
    d = int("ng04f1", 24) + x*24**3
    e = int("fkjb50ik", 24) + x*24**2
    if (a+b+c+d+e)%23 == 0:
        print(x, (a+b+c+d+e)//23)


for x in "0123456789abcdefghijklmn":
    a = int(f"4m{x}f", 24)
    b = int(f"265afdn{x}", 24)
    c = int(f"n4{x}931b3l", 24)
    d = int(f"ng{x}4f1", 24)
    e = int(f"fkjb5{x}ik", 24)
    if (a+b+c+d+e)%23 == 0:
        print(x, (a+b+c+d+e)//23)
