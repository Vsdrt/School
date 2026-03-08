from math import sqrt

a = [int(x) for x in open("17_5.txt")]
res = []

arr = [x for x in range(1, 32)]


for i in range(len(a)-1):
    x = a[i:i+2]
    if sum((sqrt(c) in arr) and (c%2==0) for c in x)==2:
        res += [sum(x)]

print(max(res), len(res))
    
