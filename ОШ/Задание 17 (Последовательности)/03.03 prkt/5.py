a = [int(x) for x in open("17_05.txt")]
mx = max(x for x in a if str(x)[-1] == "9")
res = []

for i in range(len(a) - 1):
    x = a[i:i+2]
    if (sum(str(c)[-1] == "9" for c in x) == 1) and (x[0])**2 + (x[1])**2 < mx**2:
        res += [(x[0])**2 + (x[1])**2]

print(len(res), min(res))
