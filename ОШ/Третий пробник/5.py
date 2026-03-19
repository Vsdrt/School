def solve(x):
    a = bin(x)[2:]
    a = a + str(a.count("1") % 2)
    a = a + str(a.count("1") % 2)
    return int(a, 2)


print("proverka:", solve(13))

for x in range(1, 1000000):
    if solve(x) > 80 and solve(x) < 150:
        print(solve(x))
        break