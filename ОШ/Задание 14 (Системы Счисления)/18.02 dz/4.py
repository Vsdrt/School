for x in "0123456789abcde":
    a = int(f"1{x}51", 15)
    b = int(f"3{x}2", 15)

    if (a-b)%4==0:
        print(x, (a-b)//4)
