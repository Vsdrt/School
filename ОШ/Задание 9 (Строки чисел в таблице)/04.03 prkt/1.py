res = 0

for s in open("9_01.txt",):
    a = [int(x) for x in s.split()]
    a2 = [c for c in a if a.count(c)==2]

    if len(a2)==2:
        res += 1

print(res)
