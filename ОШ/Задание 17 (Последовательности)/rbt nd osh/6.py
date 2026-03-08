a = [int(x) for x in open("17_06.txt")]
mn = min(c for c in a if c>0 and c%19==0)
res = []

for i in range(len(a) - 1):
    x = a[i:i+2]
    if sum(x)<mn:
        res += [sum(x)]

print(len(res), abs(max(res)))
