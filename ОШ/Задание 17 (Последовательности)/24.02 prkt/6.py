f = open("17_6.txt")
a = [int(x) for x in f]
mn = min(x for x in a)

res = []

for i in range(len(a) - 1):
    x = a[i:i+2]
    if sum(c%55==mn for c in x)>=1:
        res += [sum(x)]

print(len(res), min(res))
