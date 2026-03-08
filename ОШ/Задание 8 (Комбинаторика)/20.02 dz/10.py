from itertools import permutations

s = "компьютер"
res = set()

for x in permutations(s, r  = 9):
    a = "".join(x)
    perv = sorted(a[:4])
    q = ""
    for z in perv:
        q += str(z)

    if (a[-2] == "е") and (a[:4] == q):
        res.add(a)

print(len(res), res)
