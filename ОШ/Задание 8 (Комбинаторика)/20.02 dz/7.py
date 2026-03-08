from itertools import permutations

s = "sportloto"
res = set()

for x in permutations(s):
    a = "".join(x)

    if "ooo" in a:
        res.add(a)

print(len(res), res)
