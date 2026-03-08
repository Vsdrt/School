from itertools import permutations

s = "leviosa"
res = set()
for x in permutations(s):
    a = "".join(x)

    if a[0] not in "eioa" and a[3] not in "lvs":
        res.add(a)

print(len(res))
