a = [int(x) for x in open("17_4.txt")]
res = []

for i in range(len(a)-1):
    x = a[i:i+2]
    if sum(c%5==0 for c in x)==2 and sum(c%3==0 for c in x)==0:
        res += [sum(x)]

res.sort()
print(len(res), res)
