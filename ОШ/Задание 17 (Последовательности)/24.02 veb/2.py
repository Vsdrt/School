f = open("17_2.txt")
a = [int(x) for x in f]
mn = min(x for x in a if str(x)[-1] == "8")

res = []

for i in range(len(a)-1):
    x = a[i:i+2]
    if sum(c%16 == m for c in x) == 1:
        res += [sum(x)]

print(len(res), max(res))
        
