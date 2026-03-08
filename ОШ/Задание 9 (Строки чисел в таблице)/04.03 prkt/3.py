res = 0

for s in open("9_03.txt"):
    a = [int(x) for x in s.split()]
    a_3 = [c for c in a if str(c)[-1]=="3"]
    a_ot = [c for c in a if c < 0]
    a_pl = [c for c in a if c > 0]

    if len(a_3)==3 and (sum(a_pl))**2 < (sum(a_ot))**2:
        res += 1

print(res)
