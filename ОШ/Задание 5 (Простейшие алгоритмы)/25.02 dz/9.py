def solve(n):
    q = bin(n)[2:]
    s = n - q.count("0")
    s = bin(s)[2:]
    s = s[-3:] + s

    return int(s, 2)

mn = 10**10
for n in range(1, 100000):
    if solve(n) > 224:
        mn = min(solve(n), mn)

print(mn)
