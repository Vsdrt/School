for x in open("9_01.txt"):
    a = [int(c) for c in x.split()]
    a1 = [c for c in a if a.count(c)==1]
    a3 = [c for c in set(a) if a.count(c)==3]
    if len(a1)==4 and len(a3)==3 and sum(a1)//4 <= a3[0]:
        res = sum(a)

print(res)
        

    
