def solve(n):

    s = bin(n)[2:]

    kolvo = s.count("0") + s.count("1")

    if kolvo%2 == 0:
        s = s + "10"
    else:
        s = "11" + s

    return int(s, 2)

res = set()
for n in range(100, 201):
    if solve(n) % 2 == 0:
        res.add(n)

print(len(res))
        
