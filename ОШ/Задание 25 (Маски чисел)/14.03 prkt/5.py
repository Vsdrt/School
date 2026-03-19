def divs(x):
    res = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return res


for x in range(700_001, 700_200):
    deli = divs(x)
    for i in deli:
        if str(i)[-1] == "7" and i != x and i != 7:
            print(x, i)
