from itertools import permutations


s = "ольга"
res = set()

for a in permutations(s, r=5):
    x = "".join(a)

    if x[0] != "ь" and "оь" not in x and "аь" not in x:
        res.add(x)

print(res, len(res))
