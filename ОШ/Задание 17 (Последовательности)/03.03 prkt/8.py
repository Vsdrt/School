a = [int(x) for x in open("17_08.txt")]
res = []


for i in range(len(a) - 1):
    x = a[i:i+2]
    if abs(x[0]) > abs(x[1]) and sum(x)%27==0:
        res += [sum(x)]

print(len(res), abs(min(res)))
