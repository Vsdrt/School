res = 0


for s in open("9_04.txt"):
    a = sorted([int(x) for x in s.split()])
    a1 = [c for c in a if a.count(c)==1]
    
    if a[2]**2 < a[0] * a[-1]   and len(a1)==5:
        res += 1

print(res)
