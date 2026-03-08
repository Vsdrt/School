from math import prod


a = [int(x) for x in open("17_01.txt")]
res = []


for i in range(len(a) - 1):
    x = a[i:i+2]
    if prod(x)>0 and sum(x)%7==0:
        res += [prod(x)]

print(len(res), min(res))
