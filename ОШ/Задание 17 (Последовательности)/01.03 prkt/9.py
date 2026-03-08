a = [int(x) for x in open("17_9.txt")]
res = []

for i in range(len(a)):
    for k in range(i+1, len(a)):

        if (a[i] + a[k])%120==0:
            res += [a[i] + a[k]]

print(len(res), max(res))
