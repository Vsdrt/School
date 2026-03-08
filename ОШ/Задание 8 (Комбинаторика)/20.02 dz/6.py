from itertools import product

s = "венок"
res = set()

for x in product(s, repeat = 5):
    a = "".join(x)
    res.add(a)
    
k = 0
for x in sorted(res):
    k += 1
    if x.count("н")==2 and x.count("к")==2:
        print(k, x)
        
