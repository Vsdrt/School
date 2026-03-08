f = open("17_1.txt")
a = [int(x) for x in f]
mn = min(c for c in a if c > 0 and c % 35 == 0)
res = []
for i in range(len(a)-1):
    x = a[i:i+2]
    if x[0] != x[-1] and abs(x[0]- x[1]) % m == 0:
        res += [sum(x)]

print(len(res), max(res))
    
    
