a = [int(x) for x in open("17_6.txt")]
mn = min(x for x in a if x%21==0)
res = []

for i in range(len(a)-1):
    x = a[i:i+2]
    if sum(c%mn==0 for c in x)>=1:
        res += [sum(x)]

print(len(res), max(res))
