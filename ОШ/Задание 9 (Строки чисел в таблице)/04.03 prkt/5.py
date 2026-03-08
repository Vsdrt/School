res = 0


for s in open("9_05.txt"):
    a = sorted([int(c) for c in s.split()])
    a3 = [c for c in a if a.count(c)==3]
    a1 = [c for c in a if a.count(c)==1]


    if (a[0] + a[-1])**2 > (a[1])**2 + (a[2])**2 + (a[3])**2 + (a[4])**2 or\
       (len(a3) == 3 and len(a1) == 3):
        res += 1

print(res)
