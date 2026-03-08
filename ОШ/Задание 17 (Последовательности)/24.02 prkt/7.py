f = open("17_7.txt")
a = [int(x) for x in f]

res = []

for i in range(len(a) - 1):
    x = a[i:i+2]
    if sum(str(c)[-1] == "5" for c in x)==2:
        res += [sum(x)]

print(len(res), max(res))
