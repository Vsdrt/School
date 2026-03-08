for s in open("9.txt"):
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x)==1]
    a3 = [x for x in a if a.count(x)==3]

    if len(a3) == 3 and len(a1) == 4 and (sum(a1))//4 <= a3[0]:
        print(a, a1, a3)

