f = open("17_3.txt")
a = [int(x) for x in f]
mn = min(x for x in a)
res = []

for i in range(len(a)-2):
    x = a[i:i+3]

    if (sum(c<0 for c in x) > sum(c>0 for c in x)) and str(sum(x))[-1] == str(mn)[-1]:
        res += [abs(sum(x))]

print(len(res), max(res))
