f = open("17_3.txt")
a = [int(x) for x in f]
mn = min(x for x in a if 100<=x<=999 and str(x)[-1] == "7")

res = []

for i in range(len(a) - 1):
    x = a[i:i+2]
    if sum(100<=c<=999 for c in x)==1 and sum(x)%mn==0:
        res += [sum(x)]

print(len(res), min(res))
