import itertools

s = "eroslav"
res = set()
for x in itertools.permutations(s, r = 5):
    a = "".join(x)
    sogl = sum(a.count(c) for c in "rslv")
    gl = sum(a.count(c) for c in "eoa")
    
    if sogl > gl and all(s1 + s2 not in a for s1 in "eoa" for s2 in "eoa"):
        res.add(a)
        
print(len(res))
