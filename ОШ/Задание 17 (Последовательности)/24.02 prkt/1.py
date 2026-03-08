f = open("17_1.txt")
a = [int(x) for x in f]
mn = min(x for x in a if x>0 and x%19==0)
res = []

for i in range(len(a)-1):
    x = a[i:i+2]

    if sum(x) < mn:
        res += [sum(x)]

print(len(res), abs(max(res)))
