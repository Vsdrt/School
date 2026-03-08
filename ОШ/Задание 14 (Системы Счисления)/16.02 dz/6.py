for x in "0123456789abcdefgh":
    a = int(f"19{x}61", 12)
    b = int(f"3393{x}", 17)
    c = int(f"60{x}05", 15)
    if a + b == c:
        print(x, c)
        break
