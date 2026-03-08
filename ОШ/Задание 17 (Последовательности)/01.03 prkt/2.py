a = [int(x) for x in open("17_2.txt")]
res = []

for i in a:
    if i%13==7 and i%7!=0 and i%11!=0:
        res += [i]

print(max(res) - min(res), len(res))
