res = set()

for s in open("9.txt"):
    a = [int(x) for x in s.split()]
    a2 = [c for c in a if a.count(c)==2]
    a1 = [c for c in a if a.count(c) == 1]

    if len(a2)==4 and len(a1)==3 and\
       (a2[0] * a2[1] * a2[2] * a2[3]) > 2*(a1[0] * a1[1] * a1[2] ):
        print(a, a2, a1, (a2[0] * a2[1] * a2[2] * a2[3]), 2*(a1[0] * a1[1] * a1[2] ))
    
