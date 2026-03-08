def solve(n):

    s = bin(n)[2:]

    if n % 2 == 0:
        s = "10" + s
    else:
        s = "1" + s + "01"

    return int(s, 2)

print(solve(4))
print(solve(5))

for n in range(1, 9):
    print(solve(n), n)
