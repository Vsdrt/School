a = [int(x) for x in open("17_10.txt")]
mx = max(x for x in a if x%118==0 and str(x)[-1] != "8")
res = []

for i in range(len(a) - 2):
    x = a[i:i+3]
    if sum(c%118==0 for c in x)>=1 and sum(str(c)[-3:] == "118" for c in x) >=1 \
       and sum(x)>mx:
        res += [sum(x)]

print(len(res), (max(res))**2)
