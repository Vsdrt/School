a = [int(x) for x in open("17_7.txt")]
res = []

for i in range(len(a)-1):
    x = a[i:i+2]
    if abs(sum(x))%11==0:
        res += [sum(x)]

print(len(res), max(res))
