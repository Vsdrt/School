from itertools import permutations

s = "deikstra"
res = set()
for x in permutations(s, r = 6):
    a = "".join(x)

    if a.count("i") == 1 and any( "i" + c in a for c in "dkstr"):
        res.add(a)

print(len(res))
        
