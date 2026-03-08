f = open("17_9.txt")
a = [int(x) for x in f]
res = []

for i in range(len(a)-1):
    x = a[i:i+2]
    if sum(c%3==0 for c in x)>=1:
        res += [sum(x)]

print(len(res), max(res))


