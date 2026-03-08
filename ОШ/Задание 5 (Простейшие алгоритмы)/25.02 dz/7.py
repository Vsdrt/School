def solve(n):

    s = bin(n)[2:]

    s = "1"*s.count("1")

    return int(s, 2)

res = set()
for n in range(100, 1001):
    res.add(solve(n))

print(len(res))
    


