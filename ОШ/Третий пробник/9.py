from math import prod


sm = 0
k = 0

for x in open("ОШ/Третий пробник/9.txt"):
    k += 1
    a = [int(x) for x in x.split()]
    a_nepovt = [x for x in a if a.count(x) == 1]
    a_povt = [x for x in a if a.count(x) == 2 or a.count(x) == 3]
    ysl = all(
        (a[p] % 2 == 0 and a[p + 1] % 2 != 0) or (a[p] % 2 != 0 and a[p + 1] % 2 == 0)
        for p in range(len(a) - 1)
    )
    if len(a_povt) != 0:
        pr = 1
        for x in a_povt:
            pr = pr * x 
    else:
        pr = 0

    if ysl and ((3 * sum(a_nepovt)) >= pr):
        #print(3 * sum(a_nepovt), pr, a_povt)
        sm += k

print(sm)
