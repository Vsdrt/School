from itertools import permutations, product

s = "IGROK"
res = set()

for x in permutations(s):
    a = "".join(x)
    if a[0] != "K" and "ROK" not in a:
        res.add(a)
        
print(len(res), res)
