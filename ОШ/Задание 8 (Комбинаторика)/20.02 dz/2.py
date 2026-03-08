from itertools import permutations

s = "sportloto"
res = set()

for x in permutations (s, r = 9):
    a = "".join(x)
    if a[0] == "o" and a[-1] == "o":
        res.add(a)

print(len(res))
