from math import prod

a = [int(x) for x in open("17_10.txt")]

res = []

for i in range(len(a) - 1):
    x = a[i:i+2]
    if sum(x)%3==0 and sum(x)%6!=0 and str(prod(x))[-1] == "8":
        res += [sum(x)]

print(len(res), max(res))
