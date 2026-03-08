f = open("17_5.txt")
a = [int(x) for x in f]
mx = max(x for x in a if x%19==0)

res = []

for i in range(len(a) - 1):
    x = a[i:i+2]
    if sum(c>mx for c in x)>=1:
        res += [sum(x)]
print(len(res), max(res))
