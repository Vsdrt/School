for x in "0123456789abcde":
    a = int(f"99658{x}29", 15)
    b = int(f"102{x}023", 15)

    if (a + b)%14 == 0:
        print(x, (a + b)//14)
