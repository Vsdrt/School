a = [int(x) for x in open("17_06.txt")]
mn = min(x for x in a if len(str(abs(x))) == 3 and str(x)[-1] == "5")
res = []


for i in range(len(a) - 1):
    x = a[i:i+2]
    if sum(len(str(abs(c))) == 3 for c in x) == 1  and sum(x)%mn == 0:
        res += [sum(x)]

print(len(res), min(res))
