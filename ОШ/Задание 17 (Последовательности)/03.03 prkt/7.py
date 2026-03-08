a = [int(x) for x in open("17_07.txt")]
mx = max(x for x in a if x%11==0)
res = []


for i in range(len(a) - 1):
    x = a[i:i+2]
    if sum(c%11==0 for c in x)>=1 and sum(x) <= mx:
        res += [sum(x)]

print(len(res), max(res))
