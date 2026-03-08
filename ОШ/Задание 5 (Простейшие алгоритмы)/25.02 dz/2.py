def solve(n):

    s = bin(n)[2:]

    s_10 = str(int(s, 2))
    sm = 1*s_10.count("1") + 2*s_10.count("2") + 3*s_10.count("3") + \
         4*s_10.count("4") + 5*s_10.count("5") + 6*s_10.count("6") + \
         7*s_10.count("7") + 8*s_10.count("8") + 9*s_10.count("9")

    if sm % 2 != 0:
        s = s + "1"
    else:
        s = s + "0"

    s_10 = str(int(s, 2))
    sm = 1*s_10.count("1") + 2*s_10.count("2") + 3*s_10.count("3") + \
         4*s_10.count("4") + 5*s_10.count("5") + 6*s_10.count("6") + \
         7*s_10.count("7") + 8*s_10.count("8") + 9*s_10.count("9")

    if sm % 2 != 0:
        s = s + "1"
    else:
        s = s + "0"

    s_10 = str(int(s, 2))
    sm = 1*s_10.count("1") + 2*s_10.count("2") + 3*s_10.count("3") + \
         4*s_10.count("4") + 5*s_10.count("5") + 6*s_10.count("6") + \
         7*s_10.count("7") + 8*s_10.count("8") + 9*s_10.count("9")

    if sm % 2 != 0:
        s = s + "1"
    else:
        s = s + "0"
        

    return int(s, 2)



for n in range(1, 10000):
    if solve(n) > 2054:
        print(solve(n), n)
        break
