from itertools import permutations

s = "купчиха"
res  = set()

for x in permutations(s, r = 7):
    a = "".join(x)
    if not a[0] == "ч" and "иау" not in a:
        res.add(a)

print(len(res))
